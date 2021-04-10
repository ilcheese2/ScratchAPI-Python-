import os,json,requests,multiprocessing,scratchapi
from urllib.request import urlopen

os.system('npm install scratch-api')

class Get:
  def read(url):
    return json.loads(requests.get(url).text)
  class User:
    def __init__(self,user):
      self.user=user
      self.json=Get.read('https://api.scratch.mit.edu/users/'+user)
    def id(self):
      return self.json['id']
    def scratchteam(self):
      return self.json['scratchteam']
    def joindate(self):
      return self.json['history']['joined']
    def status(self):
      return self.json['status']
    def bio(self):
      return self.json['bio']
    def country(self):
      return self.json['country']
    def messages(self):
      return Get.read('https://api.scratch.mit.edu/users/'+self.user+'/messages/count')['count']
    def projects(self,amount=5):
      return Get.read('https://api.scratch.mit.edu/users/'+self.user+'/projects')[0:amount-1]
  class Project:
    def __init__(self,ProjID):
      self.Log={}
      self.ProjID=ProjID
      self.json=Get.read('https://api.scratch.mit.edu/projects/'+str(ProjID))
    def title(self):
      return self.json['title']
    def description(self):
      return self.json['description']
    def instructions(self):
      return self.json['instructions']
    def author(self):
      return self.json['author']['username']
    def created(self):
      return self.json['history']['created']
    def modfied(self):
      return self.json['history']['modified']
    def shared(self):
      return self.json['history']['shared']
    def views(self):
      return self.json['stats']['views']
    def loves(self):
      return self.json['stats']['loves']  
    def favorites(self):
      return self.json['stats']['favorites']
    def cloud(self):
      OldLog = self.Log
      try:
        self.Log = Get.read('https://clouddata.scratch.mit.edu/logs?projectid='+str(self.ProjID)+'&limit=1000&offset=0')
      except:
        self.Log = OldLog
      self.vars = {}
      for x in range(len(self.Log)):
        y = self.Log[x]
        if not '☁ ' in str(y['value']) and not y['name'][2:]in self.vars:
          self.vars.update({y['name'][2:]: y['value']})
      return self.vars
  class Studio:
    def __init__(self,StudioID):
      self.StudioID=StudioID
      self.json=Get.read('https://api.scratch.mit.edu/studios/'+str(StudioID))
    def title(self):
      return self.json['title']
    def owner(self):
      return self.json['owner']
    def created(self):
      return self.json['history']['created']
    def modified(self):
      return self.json['history']['modified']
    def followers(self):
      return self.json['stats']['followers']

class Send:
  def __init__(self,username,password):
    self.username=username
    self.password=password
    try:
      scratch=scratchapi.ScratchUserSession(username,password)
    except:
      raise Exception('Scratch login failed.')
  def SetVar(self,projId,name,value):
    Info=[str(projId),'"'+self.username+'"','"'+self.password+'"','"☁ '+name+'"',str(value)]
    with open('new.js','w') as file:
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
  def cloud(self,ProjID,VarName,VarValue):
    if not str(Get.Project(ProjID).cloud()[VarName])==str(VarValue):
      x=multiprocessing.Process(target=Send.SetVar,args=[self,ProjID,VarName,VarValue])
      x.start()
      while not str(Get.Project(ProjID).cloud()[VarName])==str(VarValue):
        pass
      x.terminate()
      os.remove('new.js')
  def follow(self,user):
    self.scratch.users.follow(user)
  def unfollow(self,user):
    self.scratch.users.unfollow(user)
  def invite(self,StudioID,user):
    self.scratch._studios_invite(StudioID,user)
  class Comment:
    def __init__(self,comment):
      self.comment=comment
    def Profile(self,user):
      self.scratch.users.comment(user,self.comment)
    def Project(self,ProjID):
      self.scratch.projects.comment(ProjID,self.comment)
    def Studio(self,StudioID):
      self.scratch.studios.send(StudioID,self.comment)
