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
You should always create a new in your forked repo for any new piece of assignment or work branching from *master* branch:

```
git branch new_branch
```

**NOTE:** You must not mess with `master` branch or BAD THINGS will happen.
*master* branch will only contain exercises, so just leave it be.

Before starting any new piece of work, move to *master* branch:

```
git checkout master
```

<br>

Now you can fetch latest changes from main repo using:

```
git fetch upstream
```

<br>

`merge` the latest code with *master* branch:

```
git merge upstream/master
```

<br>

`checkout` to your newly created branch (your branch name ideally will be your `lab_session/student_number`) :

```
git checkout new_branch
```

<br>

Rebase the code of *new_branch* from the code in *master* branch, run the `rebase` command from your current branch:

```
git rebase master
```

Now all your changes on your current branch will be based on the top of the changes in *master* branch.

Push your changes to your forked repo
```
git push origin new_branch
```
<br>

Open a pull request to the master branch so that we can check your code. You are expected to follow following topology

```
RL_Lab
│   README.md
│   Lab_session1   
│   Lab_session2   
│
└─── Student_number_1
│   │   
│   └───Lab_session1
│       │   code_1
│       │   code_2
│       │   ...
│─── Student_number_2
│   │   
│   └───Lab_session1
│       │   code_1
│       │   code_2
│       │   ...
```

w.r.t the assesment you would be asked to submit your code, instructions will follow in a seperate markdown document.
your code will be accessed only when you open pull request and mark the reviewer.

## A note about Commit Messages:
* Commit messages shouldn't span for more than 7-8 words
* Commit messages should be meaningful and not something like - "made some changes", etc.
* Never use shorthand in commit messages
* If required add a few more words about your commit messages on github/bitbucket Web Platform right before sending the pull request
* Each commit message should be structured as:
    <blockquote>(COMMIT_KEYWORD): COMMIT_MESSAGE_BODY<br><br>
Here, COMMIT_KEYWORD should take one of the values as given below - 
    1. feat - after adding a new functionality/module in existing code
    2. init - for commiting some basic code structure file, for example during the start of a new project
    3. fix - for any bug fixes
    4. merge-conflict - if there was some merge conflict in the code that you just fixed</blockquote>

## Few more points to keep in mind:
1. Always fetch the code from upstream and rebase your current branch with it, before starting with any new work.
2. Create a new branch from your master branch for any new code, so that you don't end up breaking the previous code.
4. After every small and separate change in the code, commit it

Have a look at [Git-flow](http://nvie.com/posts/a-successful-git-branching-model/) for a structured way of working with Github/bitbucket.

yolo.
