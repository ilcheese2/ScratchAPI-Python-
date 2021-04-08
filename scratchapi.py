import os, json, requests, multiprocessing
os.system('npm install scratch-api')
import scratchapi

def runJS():
  os.system('node cloud.js')

class Scratch:
  def __init__(self,username,password):
    s=scratchapi.ScratchUserSession(username, password)
    if not s.tools.verify_session():
      raise Exception('Login Failed.')
    self.username=username
    self.password=password
    self.Log=[]
  def GetVars(self, ProjID):
    OldLog = self.Log
    try:
      self.Log = json.loads(requests.get("https://clouddata.scratch.mit.edu/logs?projectid="+str(ProjID)+"&limit=1000&offset=0").text)
    except:
      self.Log = OldLog
    self.vars = {}
    for x in range(len(self.Log)):
      y = self.Log[x]
      if not "☁ " in str(y["value"]) and not y["name"][2:]in self.vars:
        self.vars.update({y["name"][2:]: y["value"]})
    return self.vars
  def GetVar(self,ProjID,VarName):
    info=self.GetVars(ProjID)
    return info[VarName]
  def GetMessages(self,user):
    self.s.users.get_message_count(user)
  def SetVar(self,ProjID,VarName,VarValue):
    with open("communicate.txt", "w") as file:
      file.write(str(ProjID)+"\n"+self.username+"\n"+self.password+"\n☁ "+VarName+"\n"+str(VarValue))
    process = multiprocessing.Process(target=runJS)
    process.start()
    while not str(self.GetVar(ProjID,VarName)) == str(VarValue):
      pass
    process.terminate()
  def Follow(self,user):
    self.s.users.follow(user)
  def Unfollow(self,user):
    self.s.users.unfollow(user)
  class Comment:
    def Profile(self,user,comment):
      self.s.users.comment(user,comment)
    def Studio(self,StudioID,comment):
      self.s.studios.comment(StudioID,comment)
    def Project(self,ProjID,comment):
      self.s.projects.comment(ProjID,comment)
