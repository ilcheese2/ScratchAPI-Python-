import os
import json
import requests
import multiprocessing
import scratchapi
from urllib.request import urlopen

os.system('npm install scratch-api')

def _Read(url):
    return json.loads(requests.get(url).text)

class User:

    def __init__(self, user):
        self.user = user
        self.json = _Read('https://api.scratch.mit.edu/users/' + user)
        self.id = self.json['id']
        self.scratchteam = self.json['scratchteam']
        self.joindate = self.json['history']['joined']
        self.status = self.json['status']
        self.bio = self.json['bio']
        self.country = self.json['country']

    #If you want you can use threading to have a loop that auto updates
    def update(self):
        self.json = _Read('https://api.scratch.mit.edu/users/' + self.user)
        self.id = self.json['id']
        self.scratchteam = self.json['scratchteam']
        self.joindate = self.json['history']['joined']
        self.status = self.json['status']
        self.bio = self.json['bio']
        self.country = self.json['country']

    def messages(self):
        return _Read('https://api.scratch.mit.edu/users/'+self.user+'/messages/count')['count']

    def projects(self):
        Info = _Read('https://api.scratch.mit.edu/users/' +
                        self.user+'/projects')
        ids = []
        for project in Info:
            ids.append(project['id'])
        return ids

    def comment(self):
        Info = urlopen(
            'https://scratch.mit.edu/site-api/comments/user/'+self.user).read().decode("utf-8")
        Message = Info[Info.index(
            '<div class="content">'):Info.index('<span class="time"')]
        Message = Message[Message.index('>')+1:Message.index('/')-1]
        Message = Message.strip()
        Author = Info[Info.index('<a href="/users/')+16:Info.index('" id')]
        return json.loads('{"Author":"'+Author+'","Message":"'+Message+'"}')

    def favorites(self):
        Info = _Read('https://api.scratch.mit.edu/users/' +
                        self.user+'/favorites')
        projects = []
        for project in Info:
            projects.append(Project(project['id']))
        return projects

class Project:
    def __init__(self, ProjID):
        self.ProjID = ProjID
        self.json = _Read(
            'https://api.scratch.mit.edu/projects/'+str(ProjID))
        self.title = self.json['title']
        self.description = self.json['description']
        self.instructions = self.json['instructions']
        self.author = self.json['author']['username']
        self.created = self.json['history']['created']
        self.modfied = self.json['history']['modified']
        self.shared = self.json['history']['shared']
        self.views = self.json['stats']['views']
        self.loves = self.json['stats']['loves']
        self.favorites = self.json['stats']['favorites']

    def update(self):
        self.json = _Read(
            'https://api.scratch.mit.edu/projects/'+str(self.ProjID))
        self.title = self.json['title']
        self.description = self.json['description']
        self.instructions = self.json['instructions']
        self.author = self.json['author']['username']
        self.created = self.json['history']['created']
        self.modfied = self.json['history']['modified']
        self.shared = self.json['history']['shared']
        self.views = self.json['stats']['views']
        self.loves = self.json['stats']['loves']
        self.favorites = self.json['stats']['favorites']

    def cloud(self):
        self.Log = _Read('https://clouddata.scratch.mit.edu/logs?projectid=' +
                            str(self.ProjID)+'&limit=1000&offset=0')
        self.vars = {}
        for x in range(len(self.Log)):
            y = self.Log[x]
            if not '☁ ' in str(y['value']) and not y['name'][2:] in self.vars:
                self.vars.update({y['name'][2:]: y['value']})
        return self.vars

    def comment(self):
        Info = urlopen('https://scratch.mit.edu/site-api/comments/project/' +
                        str(self.ProjID)).read().decode("utf-8")
        Message = Info[Info.index(
            '<div class="content">'):Info.index('<span class="time"')]
        Message = Message[Message.index('>')+1:Message.index('/')-1]
        Message = Message.strip()
        Author = Info[Info.index('<a href="/users/')+16:Info.index('" id')]
        return json.loads('{"Author":"'+Author+'","Message":"'+Message+'"}')


class Studio:

    def __init__(self, StudioID):
        self.StudioID = StudioID
        self.json = _Read('https://api.scratch.mit.edu/studios/'+str(StudioID))

    def title(self):
        return self.json['title']

    def owner(self):
        return self.json['owner']

    def created(self):
        return self.json['history']['created']

    def modified(self):
        return self.json['history']['modified']


class Send:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        try:
            self.scratch = scratchapi.ScratchUserSession(username, password)
        except:
            raise Exception('Scratch login failed.')

    def SetVar(self, projId, name, value):
        Info = [str(projId), '"'+self.username+'"', '"' +
                self.password+'"', '"☁ '+name+'"', str(value)]
        with open('new.js', 'w') as file:
            file.write('''var fs = require('fs');
    var scratch = require('scratch-api');
    function cloudVariable(projId, username, password, varName, varValue) {
    scratch.UserSession.create(username, password,  function (err, user) { 
        user.cloudSession(Number(projId),  function (err, cloud) {
        cloud.set(varName, varValue);
        });
    });
    };
    cloudVariable('''+', '.join(Info)+''')''')
        os.system('node new.js')

    def cloud(self, ProjID, VarName, VarValue):
        if not str(Project(ProjID).cloud()[VarName]) == str(VarValue):
            x = multiprocessing.Process(target=Send.SetVar, args=[
                                        self, ProjID, VarName, VarValue])
            x.start()
            while not str(Project(ProjID).cloud()[VarName]) == str(VarValue):
                pass
            x.terminate()
            os.remove('new.js')

    def follow(self, user):
        self.scratch.users.follow(user)

    def unfollow(self, user):
        self.scratch.users.unfollow(user)

    def invite(self, StudioID, user):
        self.scratch._studios_invite(StudioID, user)

    class Comment:

        def __init__(self, comment):
            self.comment = comment

        def Profile(self, user):
            self.scratch.users.comment(user, self.comment)

        def Project(self, ProjID):
            self.scratch.projects.comment(ProjID, self.comment)

        def Studio(self, StudioID):
            self.scratch.studios.send(StudioID, self.comment)
