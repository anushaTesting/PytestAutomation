# Git and GitHub 
## Why we need Git?
This is a source management software.
When we are working in a team and any automation we are working in a team, suppose if I have developed some code,and I want to share that to the team members and in the same way my team is also working on some code automation casesand they want to share that code to me.
So how we can go for this code sharing? Either we can create  a share folder and put all the code over there.But it is not a good approach because if I put some code and somebody else deleted, I will not be able to track it or I have a particular file and somebody else removed my changes. Here we use Git as a source management tool.
With the help of GIT we can manage our code, share our code.

## What is repository?
When we are sharing the code, we are placing it somwhere. It could be a shared folder or it could be a folder on the remote location. Repository is the place from where we are sharing the code.
When you are working under Git, we had to create a local repository in our system to share our codes. And one remote repository to share the folder remotely.

## What is Git and GitHub?
Git is a Source Code Management Software.
Features:
* Track changes in the file - I have created a file and placed in shared location. If somebody else is comming to change it.We can track whatever changes took place and whoever made the changes.
* Manage source files - By tracking the changes, we can well manage our source files
* Versioning and Branching - When we are working on a project, we can see lot of versions. We can manage the versions in Git.Also we can create multiple branches for the same code, so that multiple persons can work on the same piece of code.If we does not want to give any person complete access of the code, you can create a branch and give that branch location.
* Compare Code - We can compare the files to see the changes done on the file.We can compare the current file with the previous versions of the file.
* Merge Branch
* Compare Branches 

GitHub is Webbased respository hosting service.
When we are working on Git, first we create a local repository in our system, and the team members create their own local repositories in their system. Later on we will put the files from all local respository to the centrailized repository. And that centrailized repository you can find in GitHub.

Take an example:
Team member A, his machine M-A 
Team member B, his machine M-B
A centrailized repository, we can call it as remote respository.

A has created a local repository in M-A. He has written some code and put it in the local respository. And from local respository he pushed the code to Remote repository.
B takes the same code from the Remote respository and put it in his local respository. He made some changes in the code and again putting it to local repository and then to Remote respository. Again A is taking the changed code and working with it. 
You need to under stand the following terms here:
1. Commit - When you put the code to your local repository, we call COMMIT the code
2. Push - When you push the code to Remote repository from the local repository, we call PUSH the code
3. Clone - When another person(Say B) takes the code pushed to Remote repository by person A, then it is called as CLONE the code
4. Pull - When person B has cloned the code, did his work, commited to local repository and pushed to Remote respository. Now person A has to access the same code. Then it is call PULL the code.

In GitHub we are creating the remote repository.

## Setup Git and GitHub
1. Create account on Github
2. Create a remote repository
3. Set Git on the local machine

### Create account on Github(for remote repository)
* Go to https://github.com/
* sign up and verify your account
* create a new repository. Give any name for the repository. You can create only public repository as this is free.
* once created you will get the URL 'https://github.com/anushaTesting/Automation.git'

### Set Git on the local machine(for local repository)
* We need Git Bash to setup the Git on the local machine. This can be done via Visual studio code or eclipse.
* Go to https://git-scm.com/download/win and download the latest version. I downloaded
    2.22.0 64-bit version of Git for Windows. 
* Install the Git Bash
* Once it is installed, click on it from the start menu and type the command 'git --version' to see if it is installed correctly. If so it displays the git version.

## Working with Git
In order for the remote repository to identify the local repository user, we need to set up user name and email in the Git. Hence remote repository can know from which user the requests are comming.

### Global commands
Use the below global commands to set up the user name and password.
Click and open Git and type the commands

```powershell
git config --global user.name "username"
git config --global user.email "email"
```
To see the complete list of configurations done. 
```powershell
git config --list
```
### Create local repository
* Go to the location where you need to create the local repository by using the 'cd' command in git bash.
once you reached there, create a directory with 'mkdir' command. Check in your system if the folder is created. To use that folder as git repository type the command 'git init'. A hidden .git file will be created inside that folder.
Here I have created a respository named 'CodeRepository' in the location 'C://Work'

Type the following commands.
```powershell
anusha.narayan@HMECL001794 MINGW64 ~
$ cd C/Work
bash: cd: C/Work: No such file or directory

anusha.narayan@HMECL001794 MINGW64 ~
$ cd C:

anusha.narayan@HMECL001794 MINGW64 /c
$ cd Work

anusha.narayan@HMECL001794 MINGW64 /c/Work
$ mkdir CodeRepository

anusha.narayan@HMECL001794 MINGW64 /c/Work
$ cd CodeRepository

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository
$ git init
Initialized empty Git repository in C:/Work/CodeRepository/.git/

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
```

### Write/Place code in the local repository
In previous section we have created the CodeRepository. You can put the files in the folder.
Files will be in three states
1. Untracked - Whenever you are creating a file, it is untracked state. 
2. Staged - Whenever you have done with the file and when you have to share the file with team members, this is in staged state. This is an intermediate state.
3. Tracked - In this state you can share the files with the team members.

Steps to commit the code to local repository
* Your local repository here is CodeRepository in the location 'C://Work'
* Go to git bash and type the command 'pwd' to see on which directory you are. If you are not in CodeRepository go to that location
* Keep some files in CodeRepository 
* Type the command 'git status' to check the status of the files. It should be in Untracked status as we have not used those yet
* Type the git command 'git add .' for staging all files or 'git add filename' to stage that file only. Once you add the files, it will be in the intermediate status called 'Staged' and these files are ready to commit
* Now check the status 'git status'. You can see the staged files and untracked files if any.
* To commit the files to local repository type the command 'git commit -m "any informative message" to commit the files
The files in staged states will be committed to local repository
```powershell
anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ pwd
/c/Work/CodeRepository

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        results.xml
        test_body.py

nothing added to commit but untracked files present (use "git add" to track)

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git add results.xml

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   results.xml

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        test_body.py


anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   results.xml

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        EditedDocPython.pdf
        test_body.py


anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git add EditedDocPython.pdf

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   EditedDocPython.pdf
        new file:   results.xml

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        test_body.py


anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git commit -m "This is automation started"
[master (root-commit) 391cfa6] This is automation started
 2 files changed, 329 insertions(+)
 create mode 100644 EditedDocPython.pdf
 create mode 100644 results.xml

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        test_body.py

nothing added to commit but untracked files present (use "git add" to track)

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        test_body.py

nothing added to commit but untracked files present (use "git add" to track)

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$
```
### Staged to Untracked and Viceversa
Currently I have 3 files in the repository and two are commited and one new.
* Select an already committed file(results.xml) and edit it and save. It comes in untracked stage and we need to stage it inorder to commit again.
```powershell
anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   results.xml

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        test_body.py
```
* Add that file to commit . It will be in Staged state now.
```powershell
anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git add results.xml

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   results.xml

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        test_body.py

```
* To unstage (Staged to Untracked), type the command 'git reset HEAD <file>
```powershell
anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git reset HEAD results.xml
Unstaged changes after reset:
M       results.xml

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   results.xml

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        test_body.py

no changes added to commit (use "git add" and/or "git commit -a")
```
* Now two files are present in the UnTracked stage. Add them and commit.
```powershell
anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git add .

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   results.xml
        new file:   test_body.py


anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git commit -m "Commiting the two files result.xml and test_body.py"
[master fdc834d] Commiting the two files result.xml and test_body.py
 2 files changed, 14 insertions(+)
 create mode 100644 test_body.py

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master
nothing to commit, working tree clean
```
* To see all the commited files, type the command  'git log'
```powershell
$ git log
commit fdc834de5b3b1944366d0da9fad2941bc4478145 (HEAD -> master)
Author: Anusha <anusha.qaengr@gmail.com>
Date:   Wed Aug 7 14:23:19 2019 +0530

    Commiting the two files result.xml and test_body.py

commit 391cfa6ad1f1c58da9fec4dc9f18322d7966938d
Author: Anusha <anusha.qaengr@gmail.com>
Date:   Wed Aug 7 14:01:38 2019 +0530

    This is automation started
```
### Diff and Check out(To check the changes/To discard the changes)
To check the changes done on the file you can use diff command.
To dicard the changes done on the file you can use Checkout command
* Go to the CodeRepository. Select any file which is already committed. Do some changes
* Type 'git status', you can see this file as untracked
* Type 'git diff filename' to see the changes you have done in that file

```powershell
anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git diff results.xml
diff --git a/results.xml b/results.xml
index 14a9b6c..fb40f9d 100644
--- a/results.xml
+++ b/results.xml
@@ -1,4 +1,4 @@
-#Edited
+#Edited today!!
 <?xml version="1.0" encoding="utf-8"?><testsuite errors="0" failures="2" name="pytest" skipped="0" tests="9" time="12.142"><testcase classname="FixtureExamples.OnlineMarkets.Amazon.test_amazon" file="FixtureExamples\OnlineMarkets\Amazon\test_amazon.py" line="4" name="test_amazon_function" time="10.545"></testcase><testcase classname="FixtureExamples.OnlineMarkets.FlipCart.test_flipcart" file="FixtureExamples\OnlineMarkets\FlipCart\test_flipcart.py" line="3" name="test_flipkart_function" time="1.001"></testcase><testcase classname="FixtureExamples.OnlineMarkets.Myntra.test_myntra" file="FixtureExamples\OnlineMarkets\Myntra\test_myntra.py" line="4" name="test_myntra_function" time="0.005"><failure message="selenium.common.exceptions.NoSuchWindowException: Message: no such window: target window already closed
 from unknown error: web view not found
   (Session info: chrome=76.0.3809.87)">chrome_browser = &lt;selenium.webdriver.chrome.webdriver.WebDriver (session=&quot;c090c7be2a937f7d1ba4ada5d15c2b82&quot;)&gt;
```
* Now type 'git status'. You will be given two option eithe to add this file to commit or to discard the changes.
```powershell
anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   results.xml

no changes added to commit (use "git add" and/or "git commit -a")
```

* To discard the changes type the command '"git checkout -- <file>".
Now check the git status. No files to commit.
```powershell
anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git checkout -- results.xml

anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git status
On branch master
nothing to commit, working tree clean
```

## Push the code to Remote Repository
We need to follow the below steps,
1. Check the remote repository
2. Add the remote repository
3. Send local repository to remote repository

Till previous section, we have commited the files to local repository.
We have not linked local repository to Remote one, to check that type the command
```powershell
anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git remote -v
```
No result is shown.

* We have already created a remote repository in GitHub and my URL is
 https://github.com/anushaTesting/Automation.git
 * Go to git bash and type the command 'git remote add origin "Remote repository link"
 ```powershell
 anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git remote add origin "https://github.com/anushaTesting/Automation.git"

```
* Type the command 'git remote -v' to see if the link is successfully done. You can see the fetch and push repository links.
```powershell
anusha.narayan@HMECL001794 MINGW64 /c/Work/CodeRepository (master)
$ git remote -v
origin  https://github.com/anushaTesting/Automation.git (fetch)
origin  https://github.com/anushaTesting/Automation.git (push)
```
Now we have added the remote respository and checked the connection.

* To send the local repository to remote repository type the command 'git push origin master'. Master is the CodeRepository we have already in place.

```powershell
$ git push origin master
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 4 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 446.24 KiB | 19.40 MiB/s, done.
Total 8 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/anushaTesting/Automation.git
 * [new branch]      master -> master
```
* Go to the GitHub and you can see the files you have created under the repository.

### Clone Code From the Remote Repository
How other team members can fetch the code you have placed in Remote repository?
* Create another local repository in your system(as like another person creates a local repository in your system)
* In git bash go to the location of the new repository
* Type the clone command 'git clone "github url"
* once you do cloning, the files in the github will be saved in to your repository.

```powershell
anusha.narayan@HMECL001794 MINGW64 /c/Work
$ mkdir OtherPersonRepository

anusha.narayan@HMECL001794 MINGW64 /c/Work
$ cd OtherPersonRepository

anusha.narayan@HMECL001794 MINGW64 /c/Work/OtherPersonRepository
$ git clone "https://github.com/anushaTesting/Automation.git"
Cloning into 'Automation'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 10 (delta 2), reused 10 (delta 2), pack-reused 0
Unpacking objects: 100% (10/10), done.
```
Other person can now work your piece of code, in his system and can make changes commit, push etc.

### Create branches and Share the files
* I have created a new repository in Github for Pytest automation codes
https://github.com/anushaTesting/PytestAutomation.git

* In git bash, go to the folder where you have your Pytest codes
* Type the command 'git init', to make that folder as local repository
* Type the command 'git status' to check the status, all files are on untracked status now
* Type the command 'git add .' to stage all files to commit
* Type the command 'git commit -m "Comitting Pytest Codes"' , to commit to local repository
* Link the remote repository location to push the codes to remote repository
Type the command 'git remote add origin "https://github.com/anushaTesting/PytestAutomation.git"'
and check the connection by the command 'git remote -v'
You can see whether the link is established or not
* Now to push the code to remote repository type the command 'git push origin master'
* Once this is finished,go to GitHub and check if the local repository code is pushed. You can share the code to others with the link "https://github.com/anushaTesting/PytestAutomation.git"


## Jenkins Install and Setup
### Jenkins Installation
1. Install and setup JDk in your system. I have JDK 1.8 installed in my sytem.If not download, install and setup the environment variables.
2. Download the latest Jenkins war file from 'https://updates.jenkins-ci.org/download/war/'.
3. Once the jar file is downloaded, open the command prompt, go to the location where the jar file is saved.
4. Now we need to setup the Jenkins with the port number. Type the command
```powershell
java -jar "jenkins.war" --httpPort=8086
```
It will start Jenkins on your system now.
5. Go to the browser "http://localhost:8086/"
6. You can see a message to unlock the jenkins. For that go to the folder specified in the page, open the notepad file and get the secret password. Paste it under administrator password column and  click on continue
7. Once you click on continue, You can install the suggested plugins. Click on it. It starts downloading the plugin. Wait for some time
8. Once the plugins are downloaded, you get a form to create the admin user. Fill the mandatory fields , save and continue
9. The Jenkin has setup in your system. And the URL is "http://localhost:8086/".

### Jenkins Setup
On Jenkins, click on Manage Jenkins link. You need to configure
1. java path
2. python path
3. GIT path

To configure java and Git path(since they are global tool in jenkins)
* Click on Manage Jenkins -> Global Tool Configuration -> JDK
* Copy the path of JDK in your system 'C:\Program Files\Java\jdk1.8.0_221'
* Give a name say 'Java_HOME' and paste the URL, click on Apply and save
* Click on Manage Jenkins -> Global Tool Configuration -> Git
* Copy the path of GIT exe in your system 'C:/Program Files/Git/bin/git.exe'
* Give a name say 'GIT' and paste the URL, click on Apply and save

To configure python path
* Download and install python in your system
* Click on Manage Jenkins -> Configure System -> Environment Variables
* Give python path here. You need to give python home and python script path
Python_home , C:\Python37;C:\Python37\Scripts (the two paths for python_home)
Python_Scripts, C:\Python37\Scripts

Note : To restart Jenkins run this command.
```powershell
java -jar "jenkins.war" --httpPort=8086
```
### Setup Allure Reporting on Jenkins
Allure is an open-source framework designed to create interactive and comprehensive test report by Yandex QA Team. Each time when we run automation tests, we will have test results  to view details about no. of tests passed, failed and failure details etc. And few reports also include test failure screenshots.

* Install Allure plugin in Jenkins
Open Jenkins -> Manage Jenkins -> Manage Plugins -> Select Available Plugins -> Search for allure -> Install without restart
Allure plugin is installed in Jenkins.

* Download allure command line tool
Google search and you will get this site 'https://github.com/etki/allure-cli'. In that go to the page 
https://github.com/baev/allure-cli-depricated/releases/tag/allure-cli-2.4
 and download latest allure zip file. once downloaded unzip the file.

 * Configure Allure path in Jenkins
 Click on Manage Jenkins -> Global Tool Configuration -> Allure
 Give a name say Allure_Home, and give the path of Allure bin in your system 'C:\allure-cli\bin'

 To check if everything is installed correctly on Jenkins go to NewItem -> Enter any name(Say Sample job) -> FreeStyle Project and click on enter
 On this page, under Source Management Git should be present and under Post-build actions Allure report should present.

 Allure plugin will help to upload allure report on the jenkins. Allure report is in XML report. We need a command line tool to convert XML to HTML and upload it to Jenkins.

 ## Create Jobs on Jenkins
 1. Step 1 - Create job in jenkins and fetch data from Git
 * Go to Jenkins . Click on New Item and create a job. Give any name for the job and select Freestyle project and click on enter.
 * Under Source Management, select Git and give your Git repository URL 'https://github.com/anushaTesting/PytestAutomation.git'
 * Apply and save
 * You can see a job is created in Jenkins
 * Now click on Build Now to create a build
 * Once the build is created, click on the build
 * You can see several options to see the build details .
 Status, Changes, Console output etc.
 * In console ouput you can see if the code is fetched successfuly from Git.

2. Step 2 - Set Enviroment Variable and Run the batch file
We need to set up environment variable in the job we have created as per the job needs. 
Inside the job created(That is in the project) -> click on configure -> Build -> Select Execute Windows Batch Command and enter the environment variable here. If you are going to work with python set the variable as 
```powershell
Set path=%Python_Home%;%Path%
```
Add environment variable before the path variable. Enviroment variable we have already configured under Manage Jenkins -> Configure System -> Environment Variables
The final environment variable has python path and the remaining path

### Execute Jenkins with Pytest
We have explained in previous section, but the follow the steps once more
1. I have created a folder in my system, where my Pytest codes are present
2. I have pushed those code to GitHub repository
3. On Jenkins I have set up a new Job (new project)
4. On jenkins project configure -> source management -> give github repository location.
5. On jenkins project configure -> build -> select execute windows batch command -> set up the environment variables of python
6. On configure -> build -> select execute windows batch command -> give the pytest command to run(as like you are doing with pytest). Say to execute my pytest test cases marked UI, give  as pytest -m UI.
Apply and save
7. Now click on Build Now to create the build
8. You can see your test cases running in Jenkins as like in VisualStudio/Pycharm(any editor).
9. Click on console output to see the details
An example is pasted here:
```powershell
Started by user Anusha
Running as SYSTEM
Building in workspace C:\Users\anusha.narayan\.jenkins\workspace\PyTest-Git-Job
No credentials specified
 > C:/Program Files/Git/bin/git.exe rev-parse --is-inside-work-tree # timeout=10
Fetching changes from the remote Git repository
 > C:/Program Files/Git/bin/git.exe config remote.origin.url https://github.com/anushaTesting/PytestAutomation.git # timeout=10
Fetching upstream changes from https://github.com/anushaTesting/PytestAutomation.git
 > C:/Program Files/Git/bin/git.exe --version # timeout=10
 > C:/Program Files/Git/bin/git.exe fetch --tags --force --progress https://github.com/anushaTesting/PytestAutomation.git +refs/heads/*:refs/remotes/origin/*
 > C:/Program Files/Git/bin/git.exe rev-parse "refs/remotes/origin/master^{commit}" # timeout=10
 > C:/Program Files/Git/bin/git.exe rev-parse "refs/remotes/origin/origin/master^{commit}" # timeout=10
Checking out Revision d847702f1b119e8fcadd066fee7b42e2665d73ba (refs/remotes/origin/master)
 > C:/Program Files/Git/bin/git.exe config core.sparsecheckout # timeout=10
 > C:/Program Files/Git/bin/git.exe checkout -f d847702f1b119e8fcadd066fee7b42e2665d73ba
Commit message: "Comitting Pytest Codes"
 > C:/Program Files/Git/bin/git.exe rev-list --no-walk d847702f1b119e8fcadd066fee7b42e2665d73ba # timeout=10
[PyTest-Git-Job] $ cmd /c call C:\Users\ANUSHA~1.NAR\AppData\Local\Temp\jenkins5171726087267605730.bat

C:\Users\anusha.narayan\.jenkins\workspace\PyTest-Git-Job>Set path=C:\Python37;C:\Python37\Scripts;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Program Files (x86)\Intel\iCLS Client\;C:\Program Files\Intel\iCLS Client\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\MySQL\MySQL Utilities 1.6\;C:\Program Files\nodejs\;C:\Python37;C:\Python37\Scripts;C:\Users\anusha.narayan\Desktop\Python\src;C:\Program Files\Git\cmd;C:\Python37\Scripts 

C:\Users\anusha.narayan\.jenkins\workspace\PyTest-Git-Job>pytest -m UI 
============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: C:\Users\anusha.narayan\.jenkins\workspace\PyTest-Git-Job, inifile: pytest.ini
plugins: html-1.21.1, metadata-1.8.0
collected 9 items / 6 deselected / 3 selected

FixtureExamples\OnlineMarkets\Amazon\test_amazon.py .                    [ 33%]
FixtureExamples\OnlineMarkets\FlipCart\test_flipcart.py .                [ 66%]
FixtureExamples\OnlineMarkets\Myntra\test_myntra.py .                    [100%]

============================== warnings summary ===============================
c:\python37\lib\site-packages\_pytest\mark\structures.py:332
  c:\python37\lib\site-packages\_pytest\mark\structures.py:332: PytestUnknownMarkWarning: Unknown pytest.mark.UI - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,

c:\python37\lib\site-packages\_pytest\mark\structures.py:332
  c:\python37\lib\site-packages\_pytest\mark\structures.py:332: PytestUnknownMarkWarning: Unknown pytest.mark.flipkart - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,

c:\python37\lib\site-packages\_pytest\mark\structures.py:332
  c:\python37\lib\site-packages\_pytest\mark\structures.py:332: PytestUnknownMarkWarning: Unknown pytest.mark.onlineshopping - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,

c:\python37\lib\site-packages\_pytest\mark\structures.py:332
  c:\python37\lib\site-packages\_pytest\mark\structures.py:332: PytestUnknownMarkWarning: Unknown pytest.mark.engine - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,

c:\python37\lib\site-packages\_pytest\mark\structures.py:332
  c:\python37\lib\site-packages\_pytest\mark\structures.py:332: PytestUnknownMarkWarning: Unknown pytest.mark.entertainment - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,

-- Docs: https://docs.pytest.org/en/latest/warnings.html
============= 3 passed, 6 deselected, 5 warnings in 9.53 seconds ==============

C:\Users\anusha.narayan\.jenkins\workspace\PyTest-Git-Job>exit 0 
Finished: SUCCESS
```

### Generate Allure report and Upload to Jenkins
On Pytest to install allure reporting type as 
```powershell
pip install allure-pytest
```
That will install allure-pytest and allure-python-commons packages to produce report data compatible with Allure 2.

To enable Allure listener to collect results during the test execution simply add --alluredir option and provide path to the folder where results should be stored. E.g.:
```powershell
py.test --alluredir=%allure_result_folder% ./tests
```
or 
```powershell
$ pytest --alluredir=/tmp/my_allure_results
```

To see the actual report after your tests have finished, you need to use Allure commandline utility to generate report from the results.

```powershell
$ allure serve /tmp/my_allure_results
```
Refer more details on 

https://docs.qameta.io/allure/#_pytest


