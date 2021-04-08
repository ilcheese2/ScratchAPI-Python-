'''
Will add:
get cloud variable value
set cloud variable
comment on profile
comment on studio
comment on project
follow someone
unfollow someone
'''



import os, json, requests, multiprocessing

class Scratch:
	def runJS():
  	os.system("Cloud.js")
  class Cloud:
		def __init__(self,username,password):
			self.username=username
			self.password=password
		def SetVar(ProjID,VarName,VarValue):
			with open("communicate.txt", "w") as file:
      	file.write(str(self.ProjId)+"\n"+self.username+"\n"+self.password+"\n☁ "+varName+"\n"+str(varValue))
			process = multiprocessing.Process(target=runJS)
			process.start()
			while not int(self.getVar(varName)) == int(varValue):
				pass
			process.terminate()
