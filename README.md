# ICS3U
Working repo for Mr. Fabroa's Grade 11 Computer Science
 
## Set Up (One time only)

### 1) Create your ICS3U-NotesExamples Repository
* create a github account using your k12.ca
* check your email for a new assignment in github called ICS3U-NotesExamples and accept the assignment.  This will generate a new repository for you

### 2) Clone your repository
* From *your* repository StRobertCHSCS/ICS3U-NotesExamples-[your name], click on the **Clone or Download** button (the green one on the right) and copy the URL
* In vs code, load a new terminal, verify it is positioned in the default directory
* In terminal, clone your repository to your device `git clone [your repositoryurl]
* In vs code, got to `File -> open folder` and choose the new director created from the previous clone 
* repeat this for any computer you will be working on

### 3) Set the upstream remote
* in the terminal `git remote add upstream https://github.com/StRobertCHSCS/ICS3U1-FabroaNotesExamples.git`


## Day-To-Day Steps
For each class you want to
1. pull any of my updates from the upstream
2. pull any of your updates (if you made any changes from the another device i.e home)
3. copy any example files from the master to your working directory
4. edit files in your Working directory
5. Commit your changes
6. Push your changes to github

### 1. Pull changes from the upstream
`git pull upstream master`

### 2. Pull any of your updates
`git pull origin master`

### 3. copy any example files from the master to your working directory
You can use the Explorer in vs code or use the cp command in terminal when directed to copy files to the working directory

### 4. edit files in your Working directory
When working with class examples, make sure you are editing files in your Working directory

### Stage and Commit Your Changes
#### In VS Code
* click on the Source Control icon on the left in VS Code (the forked path under the search icon )
* any modified files should appear in the CHANGES section
* click on the + in the CHANGES section header
* make the necessary changes to your code or other files
* In the terminal (make sure you are in the directory of your project (type `pwd` on the terminal to verify your current directory):

* `git add yourfilename` to track a single file or `git add -A` to track all files in the project
then

```
git commit -m "type a short meaningful message in present tense about your changes"
git push origin master
```


### Pull changes from your fork on github down to a your local repository
* In the terminal, be sure your are in the directory containing your fork on your computer (type `pwd` on the terminal to verify your current directory).
* type in `git pull origin master`



### Pull Changes from the Upstream Repository
Do this when there are updates to pull from the upstream(parent) repository StRobertCHSCS/ICS4U1c-2018-19 (not your fork)
* first you will need to add and upstream remote (you only need to do this once)
    * `git remote add upstream https://github.com/[Original Owner Username]/[Original Repository].git`
    * for example `git remote add upstream https://github.com/StRobertCHSCS/ICS4U1c-2018-19.git`
* now any time you want to pull from the upstream remote: **`git pull upstream master`**


### Changing the git user name
Before you make any changes when working on the school laptops (class chromebooks),  it's a good idea to check that you are the current git user.
* To check the current git user: `git config user.name`
* To change the current git user:
```text
git config user.name "your_git_username"
git config user.email "your_git_account_email"

```







