# Virtual Environment

This part is a quick tutorial how you'll work in virtual environment, and avoid breaking global environment.
It's highly advisable you use it for your own PC.

Let's hope virtualenv is installed on your local machine.

check if it's installed 
`virtualenv --version`

if not then we are probably out of luck. But let's check if we can install it?

```
pip install virtualenv
```

### Create Virtualenv

`virtualenv <name>`

### Activate Virtualenv

if your virtualenv is not in home.

`source <path_to_name>/<name>/bin/activate`

or 
When your virtualenv is at home

`source <name>/bin/activate` 

### Install the dependencies

`pip install -r requirements.txt`