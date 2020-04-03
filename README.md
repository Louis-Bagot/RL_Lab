# RL_Lab
### Introduction
This repo is where all lab exercises and sessions for UA would be posted
It is expected of students to have a basic knowledge of github to access this repo. 

Since this will a public repo, don't add your code and follow the guidelines for using the repo. 
## Guidelines

Fork this repository to your account, using the **Fork** button on the top right corner.

Use `git clone` to clone your forked repo to your local machine:
(replace 'your_username' with appropriate value)
```
git clone https://github.com/<username>/RL_Lab.git

```
<br>

`cd` into cloned repo:
`cd <folder_name>`


Obviously setting up SSH for interacting with github is a much more secure and hassle free way.
So, it is highly recommended that you setup ssh for github/bitbucket using: [How to set up SSH - bit bucket](https://confluence.atlassian.com/bitbucket/set-up-ssh-for-git-728138079.html/).

<br>

Set the `upstream` to this repo:

The easiest way is to use the https url:
```
git remote add upstream https_url_of_repo
```

or if you have ssh set up you can use that url instead:
```
git remote add upstream ssh_url_of_repo
```

<br>

Lab assignments and exercises will always be in *master* branch.

**NOTE:** You must not mess with `master` branch or BAD THINGS will happen.
*master* branch will only contain exercises, so just leave it be.

<br>

Now you can fetch latest changes from main repo using:

```
git fetch upstream
```

Lab exercises willuse following convention:


```
RL_Lab
│   README.md
│      
│      
│
└─── Lab_session1
│   │   
│   └───code_1
│   └───code_1
│   └───code_1
│
│─── Lab_session2
│   │   
│   └───Sub_exercise_1
│       │   code_1
│       │   code_2
│       │   ...
│   └───Sub_exercise_2
│       │   code_1
│       │   code_2
│       │   ...
```

w.r.t the assesment you would be asked to submit your code, instructions will follow in a seperate PDF/markdown document.


