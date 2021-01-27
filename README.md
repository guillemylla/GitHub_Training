# GitHub Training

GitHub training for the Extavour lab

------------

## Basic bash commands

Bash is a command language for Unix shell (which means that are the same for MacOs and Linux, and different from Windows which uses DOS). 

The Bash commands that will appear in this tutorial are:

- ```cd```: change directory 
- ```mv```: move
- ```cp```: copy
- ```nano```: Commandline text editor (there are others such as vim, emacs)



----------


## What is git?


## Why do I want to use git?


## What is GitHub?


## Why do I want to use github?
- Backup
- Track versions
- Collaborate
- Download other people’s scripts


## How it works?

-------

## Hands-on

### Create a GitHub account

1. Create an account: https://github.com/join

2. Follow the steps

3. Get a "GitHub  Education" account (optional): 
	- *"If you're an educator or a researcher, you can apply to receive GitHub Team for your organization account for free."* 
	- To "upgrade"  to Educator account follow this instructions : https://docs.github.com/en/education/teach-and-learn-with-github-education/apply-for-an-educator-or-researcher-discount

### First time using git

 - The first time you use git in a computer, you need to configure it
 
 ```
 $ git config --global user.name "your_username"
 $ git config --global user.email youremail@example.com
 ```

- Optional: if you want git to remember the password during a period of time.


```
git config credential.helper 'cache --timeout=<seconds>'
```


## Repository

### Create a repository

1. Go to https://github.com/ and log in.
2. Go to your profile ("click on the top right icon"->"Your profile")
3. Click on "Repositories"
4. CLick on "New"

![](images/NewRepo1.png)

5. Choose a **name** for your repository, add a **Description** (optional) , define if it should be **public** or **private** , add a **README** file (optional), add **license** (optional).
6. "Create repository"

![](images/NewRepo2.png)

7. You will see the repository in your profile. If you chose to add a README, you will see it with its content (by defaul it will contain what you put as "Description").

![](images/NewRepo3.png)

8. Click on "Code" and copy the URL of your repostory.

![](images/NewRepo4.png)

9. Go to your computer (or the cluster, or any machine you want), open the terminal, nevigate to the directory of your choice, and **clone** the repository with the command:

```
git clone https://github.com/guillemylla/GitHub_Training.git
```
![](images/NewRepo5.png)

At this point, you have creted a repository with a README file in GitHub and downloaded it to your computer.

### Add, edit, and remove files


### Track changes

## Branch

## Track file

## Basic Git commands


- git commit
- gt push
- git stash
- git fetch
- git merge
- git pull
- git show
- git status


Other useful commands
- Cache credentials - to avoid typing pwd at every push



Hands-on example


Create new repo

My first commit


- Can I create a cloud session? connected to a public repo on my account?

```
    git add FILE
    git commit -m "my first commit"
    git push origin main
     # main used to be called "master". Github recently removed unnecessary references to slavery
``` 



## Other things

- Host your websites
- Share posters (i.e. a QR code on your poster that redirects to the PDF hosted on github )


## Resources
- http://book.git-scm.com/book/en/v2
- https://help.rc.ufl.edu/doc/Git
- https://github.com/magitz/github-slideshow 
- https://ufresearchcomputing.github.io/git-training/
- https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- https://education.github.com/git-cheat-sheet-education.pdf





