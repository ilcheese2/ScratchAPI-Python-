'''
Will add:
'''

import os, json, requests, multiprocessing

os.system('pip install scratchapi')

class Scratch:
	def __init__(username,password):
		s=scratchapi.ScratchUserSession(username, password)
		if not s.tools.verify_session():
			raise Exception('Login Failed.')
		self.username=username
		self.password=password
	def runJS():
  	os.system("Cloud.js")
	self.Log={}
	def GetVars(self, ProjID):
		OldLog = self.Log
		try:
		self.Log = json.loads(requests.get("https://clouddata.scratch.mit.edu/logs?projectid="+str(self.ProjID)+"&limit=1000&offset=0").text)
		except:
		self.Log = OldLog
		self.vars = {}
		for x in range(0, len(self.log)):
		y = self.log[x]
		if not "☁ " in str(y["value"]) and not y["name"][2:] in self.vars:
			self.vars.update({y["name"][2:]: y["value"]})
		return self.vars
	def GetVar(self,ProjID,VarName):
		return GetVars(self, ProjID)[VarName]
	def GetMessages(self,user):
		s.users.get_message_count(user)
	class Cloud:
		def SetVar(self,ProjID,VarName,VarValue):
			with open("communicate.txt", "w") as file:
      				file.write(str(self.ProjId)+"\n"+self.username+"\n"+self.password+"\n☁ "+varName+"\n"+str(varValue))
			process = multiprocessing.Process(target=runJS)
			process.start()
			while not str(self.GetVar(varName)) == str(varValue):
				pass
			process.terminate()
		def Follow(self,user):
			s.users.follow(user)
		def Unfollow(self,user)
			s.users.unfollow(user)
		class Comment:
			def Profile(self,user,comment):
				s.users.comment(user,comment)
			def Studio(self,StudioID,comment):
				s.studios.comment(StudioID,comment)
			def Project(ProjID,comment):
				s.projects.comment(ProjID,comment)
