#  **scratch3api**

A [python](www.python.com) interface for the [scratch](www.scratch.com) website
## First Use

## Getting started
The first time using the api, you need to run this:
```python
import os
os.system('npm install scratch-api')
```

## Getting Information
Class scratchapi3.Get has four subclasses:
### User('username')
Gets information about a specific user

Example use:

`print(scracth3api.Get.User('PikachuB2005').country())` will print the country set on PikachuB2005's profile

* `id()` -the users id
* `scratchteam()` -True or False
* `joindate()` -When the account was made
* `status()` -The user's What I'm Working On text
* `bio()` -The user's About Me text
* `country()` -What the user has as his/her set country
* `messages()` -How many new messages the user has
* `projects()` -A list with dictionaries of the users latest projects.
* `comment()` -Dictionary of the last comment on the profile
* `favorites()` -The ids of the user's favorite projects
### Project('Project ID')
Gets information about a project

Example use:

`print(scratch3api.Get.Project(10128407).views())` will print the number of views the project with that id has

* `title()` -The project's title
* `description()` -The project's description
* `instructions()` -The project's instructions
* `author()` -Who owns the project
* `created()` -When the project was created
* `modified()` -When the project was last saved
* `shared()` -When the project was last shared
* `views()` -The project's views
* `loves()` -The project's loves
* `favorites()` -The project's favorites
* `cloud()` -A dictionary of the project's cloud variables and their values
* `comment()` -A dictionary of the last comment on the project
### Studio('Studio ID')
Gets information about a studio

Example use:

`print(scratch3api.Get.Studio(475016).owner())` will print the name of the owner of the studio with that id

* `title()` -The studio's title
* `owner()` -The studio's owner
* `created()` -When the studio was created
* `modified()` -When the studio was last changed
* `followers()` -How many followers a studio has

## Sending Information
Requires you to sign in.
scratch3api.Send('username','password') has one subclass:
### Comment
Comments stuff

Example use:

`scratch3api.Send('PikachuB2005','MyPassword').Profile('griffpatch','Hello!')` will comment 'Hello!' on griffpatch's profile

* `Profile('username','comment')` -Comments on th e user's profile
* `Project('Project ID','comment')` -Comments on the progect
* `Studio('Studio ID','comment')` -Comments on the studio
### These are not part of a subclass
This is used to set a cloud variable

Example use:

`scratch3api.Send.cloud(513819954,'test',108)` will set the cloud variable named ???test in the project with that id to 108

* `cloud('Project ID','Variable Name','Variable Value')`

These are used for following:
* `follow(username)` -Follows the user
* `unfollow(username)` -Unfollows the user

Invite someone to a studio:
* `invite('Studio ID','username')` -Invites the user to the studio with that id

