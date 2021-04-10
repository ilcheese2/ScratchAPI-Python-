#  **scratch3api**

A [python](www.python.com) interface for the [scratch](www.scratch.com) website

## Getting Information
Class scratchapi3.Get has three subclasses:
### User('username')
Gets information about a specific user
* `id()` -the users id
* `scratchteam(
)` -True or False
* `joindate()` -When the account was made
* `status()` -The user's What I'm Working On text
* `bio()` -The user's About Me text
* `country()` -What the user has as his/her set country
* `messages()` -How many new messages the user has
* `projects(amount=5)` -A list with dictionaries of the users latest projects. The amount shown can be changed.
### Project('Project ID')
Gets information about a project
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
### Studio
Gets information about a studio
* `title()` -The studio's title
* `owner()` -The studio's owner
* `created()` -When the studio was created
* `modified()` -When the studio was last changed
* `followers()` -How many followers a studio has
## Sending Information
Requires you to sign in.
scratch3api.Send('username','password') has one subclass:
### Comment
* `Profile('username','comment')`
* `Project('Project ID','comment')`
* `Studio('Studio ID','comment')`
### These are not part of a subclass
This is used to set a cloud variable:
* `cloud('Project ID','Variable Name','Variable Value')`

These are used for following:
* `follow(username)`
* `unfollow(username)`

Invite someone to a studio:
* `invite('Studio ID','username')`

# Planned Updates
I have to get these in raw html, so it'll be harder for me to program them:
* Reading comments
* Reading your 'What's Happening' Section
* Reading user activity
* Finding projects a user recenty viewed, loved, or favorited
* Following/Unfollowing topic forums
