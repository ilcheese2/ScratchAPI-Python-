# ScratchAPI-Python

An API interface for [Scratch](https://scratch.mit.edu), written in [Python](https://www.python.org/).

## Getting Started
To use the api, you must log in to your scratch account:
```python
import scratchapi
scratch = Scratch('Username','Password')
```
## After Login
There are several things you can do after you are signed in.

* [`Cloud`](#Cloud)
* [`Following`](#Following)
* [`Commenting`](#Commenting)

### Cloud
<a name="Cloud"></a>
To get a dictionary of the cloud variables and their values:
```python
scratch.GetVars('Project ID')
```
To get the value of an individual variable:
```python
scratch.GetVar('Project ID','Variable Name')
```
To set a cloud variable:
```python
scratch.SetVar('Project ID','Variable Name','Variable Value')
```

### Following
<a name="Following"></a>
```python
scratch.follow('user')
scratch.unfollow('user')
```

### Commenting
<a name="Commenting"></a>
```python
scratch.Comment.Profile('user','comment')
scratch.Comment.Studio('Studio ID','comment')
scratch.Comment.Project('Project ID','comment')
```

### Credits
Credit to [Classfied3D](https://scratch.mit.edu/users/Classfied3D/) for helping with the cloud manipulation.
