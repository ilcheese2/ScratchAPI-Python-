# ScratchAPI-Python-Installer
A web API interface for [Scratch](https://scratch.mit.edu), written in [Python](https://www.python.org/).

## You have two options to get the installer:
### Do it manually
Download the .zip and extract the Installer.py file. 
Then upload the file into whatever you are running the file on (I recommend [Replit](https://replit.com))
## or
### Run this in python
```python
import subprocess
subprocess.call('git clone https://github.com/pikachub2005/ScratchAPI-Python-Installer', shell = True)
```
Move the installer file into the same folder that the previous file is in.

## Then run this:
```python
import Installer
Installer.Install()
```
And you're all set! Run the file, and you will get everything you need. A markdown file will appear telling you how to use it.
## Future Updates:
* Scratch total project count
* Info about individual users
* Info about individual projects
* Reading comments from profiles, projects, and studios
* Accessing your "What's happening?" section
* Projects you recently viewed
* Projects you recently favorited
* Projects you recently loved
* Following/ Unfollowing a studio
* Info about a users activity
* Following/Unfollowing topics on the forums
