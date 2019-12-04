from tkinter import *

total = 0
total_second = 0
total_third = 0
total_fourth = 0
total_fifth = 0
total_sixth = 0
total_seventh = 0
total_eighth = 0
total_ninth = 0
total_tenth = 0
total_eleventh = 0
total_twelfth = 0

first_set_questions = [

"Create empty Git repo in specified directory. \nRun with no arguments to initialize \nthe current directory as a git repository.",
"Clone repo located at <repo> onto local machine.",
"Define author name to be used for all commits in current repo.",
"Stage all changes in <directory> for the next commit."

]


first_set_answers_0 = ["Who dunnit","get n eat","git init","git create"]
first_set_answers_1 = ["git clown beppo","git log clone","git repo cloning","git clone <repo>"]
first_set_answers_2 = ["git author","git config user.name <name>","git name","git who"]
first_set_answers_3 = ["git get to stage","git change stage","git add <directory>","git move it"]

second_set_questions =[
   "Create new commit that undoes all of the changes made in <commit>. \nApply it to the current branch.",
   "Remove <file> from the staging area, but leave the working directory unchanged. \nThis unstages a file without overwriting any changes.",
   "Show unstaged changes between your index and working directory.",
   "Shows which files would be removed from working directory. \nUse the -f flag in place of the -n flag to execute the clean."
]

second_set_answers_0 =["git revert<commit>","git all change","git back to the future","git old branch back"]
second_set_answers_1 =["git remove still","git stage new","git reset <file>","git same old"]
second_set_answers_2 =["git minus","git diff","git new diff ","git unstaged index"]
second_set_answers_3 =["git wash -n","git scrub -n","git unscruff -n","git clean -n"]


third_set_questions =[
   "Display the entire commit history using the default format.",
   "Replace the last commit with the staged changes and last commit combined. \nUse with nothing staged to edit the last commit’s message.",
   "Rebase the current branch onto <base>. <base> can be a commit ID, \na branch name, a tag, or a relative reference to HEAD.",
   "Show a log of changes to the local repository’s HEAD. \nAdd --relative-date flag to show date info or --all to show all refs."
]

third_set_answers_0 =["git chronology","git bio","git log","git def form"]
third_set_answers_1 =["git commit --amend","git state --amend","git more -- staged","git message -- last"]
third_set_answers_2 =["git ace of base","git rebase <base>","git basic re","git re ref"]
third_set_answers_3 =["git log cranium","git change hat","git dorian gray","git reflog"]


fourth_set_questions =[
   "List which files are staged, unstaged, and untracked.",
   "List all of the branches in your repo.\n Add a <branch> argument to create a new branch with the name <branch>.",
   "Create and check out a new branch named <branch>.\n Drop the -b flag to checkout an existing branch.",
   "Merge <branch> into the current branch."
]

fourth_set_answers_0 =["git actors","git status","git listing","git parchment"]
fourth_set_answers_1 =["git oak","git sapling","git branch","git bamboo"]
fourth_set_answers_2 =["git checkout -b <branch>","git lookout -b","george watch out for that tree","git check green"]
fourth_set_answers_3 =["git meld <branch> ","git merge <branch>","git soldering <branch>","git together<branch>"]



fifth_set_questions =[
   "Create a new connection to a remote repo.\n After adding a remote, you can use <name> as a shortcut for <url> in other commands.",
   "Fetch a specific <branch>, from the repo. \nLeave off <branch> to fetch all remote refs.",
   "Fetch the specified remote’s copy of current branch \nand immediately merge it into the local copy.",
   "Push the branch to <remote>, along with necessary commits and objects. \nCreate named branch in the remote repo if it doesn’t exist."
]

fifth_set_answers_0 =["git remote add<name> <url>","git remote shortname","git remote nickname","git remote plus<name> <url>"]
fifth_set_answers_1 =["git grab<remote> <branch>","git take <remote> <branch>","git fetch<remote> <branch>","git pitch<remote> <branch>"]
fifth_set_answers_2 =["git bull <remote>","git pull <remote>","git pullimergize <remote>","git pull over"]
fifth_set_answers_3 =["git create push branch","git push objects branch","git pushy","git push<remote> <branch>"]


sixth_set_questions =[
   "Define the author name to be used for all commits by the current user.",
   "Define the author email to be used for all commits by the current user.",
   "Set text editor used by commands for all users on the machine. \n<editor> arg should be the command that launches the desired editor (e.g., vi).",
   "Open the global configuration file in a text editor for manual editing."
]

sixth_set_answers_0 =["git def author.name","git note user.name","git config --global user.name <name>","git sign pulitzer.name"]
sixth_set_answers_1 =["git config --global user.email <email>","git config world user.email","git config me.email","git user.email me sign"]
sixth_set_answers_2 =["git type system.editor","git config --systemcore.editor <editor>","git all pen config editor","git new command.editor config"]
sixth_set_answers_3 =["git open global all config","git config --worldwide --type","git all config --manual","git config --global --edit"]


seventh_set_questions =[
   "Condense each commit to a single line.",
   "Display the full diff of each commit.",
   "Search for commits by a particular author.",
   "--graph flag draws a text based graph of commits on left side of commit msgs.\n --decorate adds names of branches or tags of commits shown"
]

seventh_set_answers_0 =["git log --justone","git log --oneline","git log --strike","git log --delineate"]
seventh_set_answers_1 =["git log -fulldiff","git log -eachfull","git log -p","git log --alpha --omega"]
seventh_set_answers_2 =["git log --author=”<pattern>”","git log --they=","git log --coder","git log --who"]
seventh_set_answers_3 =["git log --graphic --deco","git log --graph --decorate","git log --flag graph deco","git log --beautigraph"]


eighth_set_questions =[
   "Show difference between working directory and last commit.",
   "Show difference between staged changes and last commit.",
   "Tokenize added and removed lines by whitespace and then diff those.", #git diff --color-words
   "Pair up matching lines of diff output and highlight sub-word fragments that have changed." #git diff-highlight
]

eighth_set_answers_0 =["git diff HEAD","git whatsnew UP","git notsame HAT","git different FACE"]
eighth_set_answers_1 =["git diff staged","git diff last","git diff --cached","git diff --new"]
eighth_set_answers_2 =["git tokediff","git diff --color-words","git diff --rainbow","git diff --white"]
eighth_set_answers_3 =["git diff-skylight","git diff-bradmondo","git diff-pairlight","git diff-highlight"]



ninth_set_questions =[
   "Reset staging area to match most recent commit, \nbut leave the working directory unchanged.",
   "Reset staging area and working directory to match most recent commit \nand overwrites all changes in the working directory",
   "Move the current branch tip backward to <commit>, \nreset the staging area to match, but leave the working directory alone.",
   "Reset both the staging area & working directory to match. \nDelete uncommitted changes, and all commits after <commit>."
]

ninth_set_answers_0 =["git tabula --rasa","git restage","git reset","git reput"]
ninth_set_answers_1 =["git reset --hard","git reset --strong","git reset --super","git reset --solid"]
ninth_set_answers_2 =["git resist","git reset <commit>","git matchify","git tip branch"]
ninth_set_answers_3 =["git area new","git reset --both","git reset stage&dir","git reset --hard <commit>"]


tenth_set_questions =[
   "Interactively rebase current branch onto <base>. \nLaunches editor to enter commands for how each commit will be transferred to the new base.",
   "Rebase - use commit", #pick
   "Rebase - use commit, but meld into previous commit", #squash
   "Rebase - remove commit"#drop
]

tenth_set_answers_0 =["git rebase interact","git rebase -i<base>","git rebase --enter","git launch rebase"]
tenth_set_answers_1 =["pock","puck","pick","pack"]
tenth_set_answers_2 =["squash","crush","splat","butternut"]
tenth_set_answers_3 =["fall","drop","release","tear"]


eleventh_set_questions =[
   "Fetch the remote content but do not create a new merge commit.", #git pull --no-commit 
   "Give verbose output during a pull which displays the content \nbeing downloaded and the merge details.", # git pull --verbose
   " Integrate the remote branch with the local one.", #git pull --rebase  
   "Fetch the remote’s copy of current branch and rebases it into the local copy. \nUses git rebase instead of merge to integrate the branches."
]

eleventh_set_answers_0 =["git pull --no-commit","git no merge pull","git full --no-new","git nope pull"]
eleventh_set_answers_1 =["git pull --chatty","git pull --chatterbox","git pull --verbose","git pull --verbal"]
eleventh_set_answers_2 =["git pull --regrate","git pull --rebase","git pull --base-one","git pull --basify"]
eleventh_set_answers_3 =["git pull --relocalize","git pull --base-over","git pull --fetchify","git pull --rebase <remote>"]



twelfth_set_questions =[
   "Force the git push even if it results in a non-fast-forward merge. \nDo not use the --force flag unless you’re absolutely sure you know what you’re doing.",
   "Push all of your local branches to the specified remote",
   "Tags aren’t automatically pushed when you push a branch or use the --all flag. \nThe --tags flag sends all of your local tags to the remote repo.",
   "Establish a tracking connection between the local \nand the newly created remote branch."#git push -u
]

twelfth_set_answers_0 =["git punch --combo","git push --strong","git push <remote> --force","git merge --sayan"]
twelfth_set_answers_1 =["git push <remote> --all","git nudge --all","git rush --most","git push --total"]
twelfth_set_answers_2 =["git push --ticket","git push <remote> --tags","git push --stamp","git push --card"]
twelfth_set_answers_3 =["git track new","git setup connection","git between push","git push -u"]


def bfirst_set():

   global windows
   windows = Toplevel(root)
   windows.title("Question 1")
   windows.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows,text = first_set_questions[0],font = ('arial',10,'bold'), bg='#aeea00' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows, text=first_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v0, indicator = 0, command = checked, bg = '#e4ff54')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows, text=first_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v0, indicator = 0, command = checked, bg = '#e4ff54')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows, text=first_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v0, indicator = 0, command = checked, bg = '#e4ff54')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows, text=first_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v0, indicator = 0, command = checked, bg = '#e4ff54')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows,text = "back",font = ('arial',12,'bold'), bg='#e4ff54', command = bback_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows,text = "next",font = ('arial',12,'bold'),bg = '#79b700', command = bfirst_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows.mainloop()


def bfirst_set_2():

   global windows3
   windows3 = Toplevel(windows)
   windows3.title("Question 2")
   windows3.geometry("600x300+300+300")
   windows.withdraw()

   lbl1 = Label(windows3, text=first_set_questions[1], font=('arial', 10, 'bold'), bg='#aeea00')
   lbl1.pack(fill=X, ipady=15, side = TOP)
   

   rb1 = Radiobutton(windows3, text=first_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v1, indicator = 0, command = checked, bg = '#e4ff54')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows3, text=first_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v1, indicator = 0, command = checked, bg = '#e4ff54')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows3, text=first_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v1, indicator = 0, command = checked, bg = '#e4ff54')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows3, text=first_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v1, indicator = 0, command = checked, bg = '#e4ff54')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows3, text = "back", font = ('arial',12,'bold'), bg='#e4ff54', command = bfrom3_to_1)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows3, text = "next", font = ('arial',12,'bold'), bg = '#79b700', command = bfirst_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows3.mainloop()


def bfirst_set_3():

   global windows4
   windows4 = Toplevel(windows3)
   windows4.title("Question 3")
   windows4.geometry("600x300+300+300")
   windows3.withdraw()

   lbl1 = Label(windows4, text=first_set_questions[2], font=('arial', 10, 'bold'), bg='#aeea00')
   lbl1.pack(fill=X, ipady=15, side = TOP)


   rb1 = Radiobutton(windows4, text=first_set_answers_2[0], font = ('arial',10,'bold'), value=0,variable = v2, indicator = 0, command = checked, bg = '#e4ff54')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows4, text=first_set_answers_2[1], font = ('arial',10,'bold'), value=1,variable = v2, indicator = 0, command = checked, bg = '#e4ff54')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows4, text=first_set_answers_2[2], font = ('arial',10,'bold'), value=2,variable = v2, indicator = 0,  command = checked, bg = '#e4ff54')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows4, text=first_set_answers_2[3], font = ('arial',10,'bold'), value=3,variable = v2, indicator = 0, command = checked, bg = '#e4ff54')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows4, text = "back", font = ('arial',12,'bold'), bg='#e4ff54', command = bfrom4_to_3)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows4, text = "next", font = ('arial',12,'bold'), bg = '#79b700', command = bfirst_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows4.mainloop()


def bfirst_set_4():

   global windows5
   windows5 = Toplevel(windows4)
   windows5.title("Question 4")
   windows5.geometry("600x300+300+300")
   windows4.withdraw()

   lbl1 = Label(windows5, text=first_set_questions[3], font=('arial', 10, 'bold'), bg='#aeea00')
   lbl1.pack(fill=X, ipady=15, side = TOP)
   
   rb1 = Radiobutton(windows5, text=first_set_answers_3[0], font = ('arial',10,'bold'), value=0,variable = v3, indicator = 0, command = checked, bg = '#e4ff54')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows5, text=first_set_answers_3[1], font = ('arial',10,'bold'), value=1,variable = v3, indicator = 0, command = checked, bg = '#e4ff54')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows5, text=first_set_answers_3[2], font = ('arial',10,'bold'), value=2,variable = v3, indicator = 0, command = checked, bg = '#e4ff54')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows5, text=first_set_answers_3[3], font = ('arial',10,'bold'), value=3,variable = v3, indicator = 0,  command = checked, bg = '#e4ff54')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows5, text = "back",font = ('arial',12,'bold'), bg='#e4ff54', command = bfrom5_to_4)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows5, text = "next",font = ('arial',12,'bold'), bg = '#79b700', command = bfirst_set_5)
   btn2.pack(padx=15, ipady=5, side=RIGHT)

   windows5.mainloop()


def bfirst_set_5():

   global windows6
   windows6 = Toplevel(windows5)
   windows6.title("Final Result")
   windows6.geometry("600x300+300+300")
   windows5.withdraw()
  
   lbl_score = Label(windows6,text = "Your score is " + str(total) + "/4",font = ("arial",12,"bold"), bg='#ff1744')
   lbl_score.pack(fill=X, ipady=15, side = TOP)
   lbl_correct_answers = Label(windows6, text='The correct answers are: \ngit init\ngit clone <repo>\ngit config user.name <name>\n git add <directory>', font=('arial', 12, 'bold'), bg='#ff616f' )
   lbl_correct_answers.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows6, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command= bfrom6_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows6, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows6.destroy)
   btn2.pack(side=RIGHT)

   windows6.mainloop()


def bsecond_set():
      
   global windows7
   windows7 = Toplevel(root)
   windows7.title("Question 1")
   windows7.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows7,text = second_set_questions[0],font = ('arial',10,'bold'), bg='#64dd17' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows7, text=second_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v4, indicator = 0, command = checked_second, bg = '#9cff57')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows7, text=second_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v4, indicator = 0, command = checked_second, bg = '#9cff57')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows7, text=second_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v4, indicator = 0, command = checked_second, bg = '#9cff57')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows7, text=second_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v4, indicator = 0, command = checked_second, bg = '#9cff57')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows7, text = "back",font = ('arial',12,'bold'), bg='#9cff57', command = bfrom7_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows7, text = "next",font = ('arial',12,'bold'),bg = '#1faa00', command = bsecond_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows7.mainloop()

def bsecond_set_2():

   global windows8
   windows8 = Toplevel(windows7)
   windows8.title("Question 2")
   windows8.geometry("600x300+300+300")
   windows7.withdraw()

   lbl1 = Label(windows8, text=second_set_questions[1], font=('arial', 10, 'bold'), bg='#64dd17')
   lbl1.pack(fill=X, ipady=15, side = TOP)
   

   rb1 = Radiobutton(windows8, text=second_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v5, indicator = 0, command = checked_second, bg = '#9cff57')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows8, text=second_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v5, indicator = 0, command = checked_second, bg = '#9cff57')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows8, text=second_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v5, indicator = 0, command = checked_second, bg = '#9cff57')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows8, text=second_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v5, indicator =0, command = checked_second, bg = '#9cff57')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows8, text = "back", font = ('arial',12,'bold'), bg='#9cff57', command = bfrom8_to_7)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows8, text = "next", font = ('arial',12,'bold'), bg = '#1faa00', command = bsecond_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows8.mainloop()

def bsecond_set_3():

   global windows9
   windows9 = Toplevel(windows8)
   windows9.title("Question 3")
   windows9.geometry("600x300+300+300")
   windows8.withdraw()

   lbl1 = Label(windows9, text=second_set_questions[2], font=('arial', 10, 'bold'), bg='#64dd17')
   lbl1.pack(fill=X, ipady=15, side = TOP)


   rb1 = Radiobutton(windows9, text=second_set_answers_2[0], font = ('arial',10,'bold'), value=0,variable = v6, indicator = 0, command = checked_second, bg = '#9cff57')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows9, text=second_set_answers_2[1], font = ('arial',10,'bold'), value=1,variable = v6, indicator = 0, command = checked_second, bg = '#9cff57')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows9, text=second_set_answers_2[2], font = ('arial',10,'bold'), value=2,variable = v6, indicator = 0, command = checked_second, bg = '#9cff57')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows9, text=second_set_answers_2[3], font = ('arial',10,'bold'), value=3, variable = v6, indicator = 0, command = checked_second, bg = '#9cff57')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows9, text = "back", font = ('arial',12,'bold'), bg='#9cff57', command = bfrom9_to_8)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows9, text = "next", font = ('arial',12,'bold'), bg = '#1faa00', command = bsecond_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows9.mainloop()
   
def bsecond_set_4():

   global windows10
   windows10 = Toplevel(windows9)
   windows10.title("Question 4")
   windows10.geometry("600x300+300+300")
   windows9.withdraw()

   lbl1 = Label(windows10, text=second_set_questions[3], font=('arial', 10, 'bold'), bg='#64dd17')
   lbl1.pack(fill=X, ipady=15, side = TOP)
   
   rb1 = Radiobutton(windows10, text=second_set_answers_3[0], font = ('arial',10,'bold'), value=0,variable = v7, indicator = 0, command = checked_second, bg = '#9cff57')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows10, text=second_set_answers_3[1], font = ('arial',10,'bold'), value=1,variable = v7, indicator =0, command = checked_second, bg = '#9cff57')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows10, text=second_set_answers_3[2], font = ('arial',10,'bold'), value=2,variable = v7, indicator = 0, command = checked_second, bg = '#9cff57')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows10, text=second_set_answers_3[3], font = ('arial',10,'bold'), value=3,variable = v7, indicator = 0, command = checked_second, bg = '#9cff57')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows10, text = "back",font = ('arial',12,'bold'), bg='#9cff57', command = bfrom10_to_9)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows10, text = "next",font = ('arial',12,'bold'), bg = '#1faa00', command = bsecond_set_5)
   btn2.pack(padx=15, ipady=5, side=RIGHT)

   windows10.mainloop()



def bsecond_set_5():

   global windows11
   windows11 = Toplevel(windows10)
   windows11.title("Final Result")
   windows11.geometry("600x300+300+300")
   windows10.withdraw()
  
   lbl1 = Label(windows11, text = "Your score is " + str(total_second) + "/4",font = ("arial",12,"bold"), bg='#ff1744')
   lbl1.pack(fill=X, ipady=15, side = TOP)
   lbl2 = Label(windows11, text='The correct answers are: \ngit revert<commit> \ngit reset <file> \ngit diff \ngit clean -n', font=('arial', 12, 'bold'), bg='#ff616f' )
   lbl2.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows11, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command=bfrom11_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows11, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows11.destroy)
   btn2.pack(side=RIGHT)

   windows11.mainloop()



def bthird_set():

   global windows12
   windows12 = Toplevel(root)
   windows12.title("Question 1")
   windows12.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows12,text = third_set_questions[0], font = ('arial',10,'bold'), bg='#00c853' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows12, text=third_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v8, indicator = 0, command = checked_third , bg = '#5efc82')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows12, text=third_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v8, indicator = 0, command = checked_third , bg = '#5efc82')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows12, text=third_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v8, indicator = 0, command = checked_third, bg = '#5efc82')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows12, text=third_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v8, indicator = 0, command = checked_third, bg = '#5efc82')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows12, text = "back", font = ('arial',12,'bold'), bg='#5efc82', command = bfrom12_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows12, text = "next",font = ('arial',12,'bold'), bg = '#009624', command = bthird_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows12.mainloop()


def bthird_set_2():

   global windows13
   windows13 = Toplevel(windows12)
   windows13.title("Question 2")
   windows13.geometry("600x300+300+300")
   windows12.withdraw()

   lbl1 = Label(windows13, text=third_set_questions[1], font=('arial', 10, 'bold'), bg='#00c853')
   lbl1.pack(fill=X, ipady=15, side = TOP)
   

   rb1 = Radiobutton(windows13, text=third_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v9, indicator = 0, command = checked_third, bg = '#5efc82')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows13, text=third_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v9, indicator = 0, command = checked_third, bg = '#5efc82')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows13, text=third_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v9, indicator = 0, command = checked_third, bg = '#5efc82')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows13, text=third_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v9, indicator = 0, command = checked_third, bg = '#5efc82')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows13, text = "back", font = ('arial',12,'bold'), bg='#5efc82', command = bfrom13_to_12)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows13, text = "next", font = ('arial',12,'bold'), bg = '#009624', command = bthird_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows13.mainloop()


def bthird_set_3():

   global windows14
   windows14 = Toplevel(windows13)
   windows14.title("Question 3")
   windows14.geometry("600x300+300+300")
   windows13.withdraw()

   lbl1 = Label(windows14, text=third_set_questions[2], font=('arial', 10, 'bold'), bg='#00c853')
   lbl1.pack(fill=X, ipady=15, side = TOP)


   rb1 = Radiobutton(windows14, text=third_set_answers_2[0], font = ('arial',10,'bold'), value=0,variable = v10, indicator = 0, command = checked_third, bg = '#5efc82')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows14, text=third_set_answers_2[1], font = ('arial',10,'bold'), value=1,variable = v10, indicator = 0, command = checked_third, bg = '#5efc82')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows14, text=third_set_answers_2[2], font = ('arial',10,'bold'), value=2,variable = v10, indicator = 0, command = checked_third, bg = '#5efc82')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows14, text=third_set_answers_2[3], font = ('arial',10,'bold'), value=3,variable = v10, indicator = 0, command = checked_third, bg = '#5efc82')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows14, text = "back", font = ('arial',12,'bold'), bg='#5efc82', command = bfrom14_to_13)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows14, text = "next", font = ('arial',12,'bold'), bg = '#009624', command = bthird_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows14.mainloop()
   

def bthird_set_4():

   global windows15
   windows15 = Toplevel(windows14)
   windows15.title("Question 4")
   windows15.geometry("600x300+300+300")
   windows14.withdraw()

   lbl1 = Label(windows15, text=third_set_questions[3], font=('arial', 10, 'bold'), bg='#00c853')
   lbl1.pack(fill=X, ipady=15, side = TOP)
   
   rb1 = Radiobutton(windows15, text=third_set_answers_3[0], font = ('arial',10,'bold'), value=0, variable = v11, indicator = 0, command = checked_third, bg = '#5efc82')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows15, text=third_set_answers_3[1], font = ('arial',10,'bold'), value=1, variable = v11, indicator = 0, command = checked_third, bg = '#5efc82')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows15, text=third_set_answers_3[2], font = ('arial',10,'bold'), value=2, variable = v11, indicator = 0, command = checked_third, bg = '#5efc82')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows15, text=third_set_answers_3[3], font = ('arial',10,'bold'), value=3, variable = v11, indicator = 0, command = checked_third, bg = '#5efc82')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows15,text = "back",font = ('arial',12,'bold'), bg='#5efc82', command = bfrom15_to_14)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows15,text = "next",font = ('arial',12,'bold'), bg = '#009624', command = bthird_set_5)
   btn2.pack(padx=15, ipady=5, side=RIGHT)

   windows15.mainloop()


def bthird_set_5():

   global windows16
   windows16 = Toplevel(windows15)
   windows16.title("Final Result")
   windows16.geometry("600x300+300+300")
   windows15.withdraw()
  
   lb_score = Label(windows16, text = "Your score is " + str(total_third) + "/4", font = ("arial",12,"bold"), bg='#ff1744')
   lb_score.pack(fill=X, ipady=15, side = TOP)
   lb_correct_answers = Label(windows16, text='The correct answers are: \ngit log \ngit commit --amend \ngit rebase <base> \n git reflog', font=('arial', 12, 'bold'), bg='#ff616f' )
   lb_correct_answers.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows16, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command=bfrom16_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows16, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows16.destroy)
   btn2.pack(side=RIGHT)

   windows16.mainloop()


def bfourth_set():

   global windows17
   windows17 = Toplevel(root)
   windows17.title("Question 1")
   windows17.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows17,text = fourth_set_questions[0],font = ('arial',10,'bold'), bg='#00bfa5' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows17, text=fourth_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v12, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows17, text=fourth_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v12, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows17, text=fourth_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v12, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows17, text=fourth_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v12, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows17,text = "back",font = ('arial',12,'bold'), bg='#5df2d6', command = bfrom17_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows17,text = "next",font = ('arial',12,'bold'),bg = '#008e76', command = bfourth_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows17.mainloop()


def bfourth_set_2():

   global windows18
   windows18 = Toplevel(windows17)
   windows18.title("Question 2")
   windows18.geometry("600x300+300+300")
   windows17.withdraw()

   lbl1 = Label(windows18,text = fourth_set_questions[1],font = ('arial',10,'bold'), bg='#00bfa5' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows18, text=fourth_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v13, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows18, text=fourth_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v13, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows18, text=fourth_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v13, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows18, text=fourth_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v13, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows18,text = "back",font = ('arial',12,'bold'), bg='#5df2d6', command = bfrom18_to_17)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows18,text = "next",font = ('arial',12,'bold'),bg = '#008e76', command = bfourth_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows18.mainloop()
   


def bfourth_set_3():

   global windows19
   windows19 = Toplevel(windows18)
   windows19.title("Question 3")
   windows19.geometry("600x300+300+300")
   windows18.withdraw()

   lbl1 = Label(windows19,text = fourth_set_questions[2],font = ('arial',10,'bold'), bg='#00bfa5' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows19, text=fourth_set_answers_2[0], font = ('arial',10,'bold'), value=0, variable = v14, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows19, text=fourth_set_answers_2[1], font = ('arial',10,'bold'), value=1, variable = v14, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows19, text=fourth_set_answers_2[2], font = ('arial',10,'bold'), value=2, variable = v14, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows19, text=fourth_set_answers_2[3], font = ('arial',10,'bold'), value=3, variable = v14, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows19,text = "back",font = ('arial',12,'bold'), bg='#5df2d6', command = bfrom19_to_18)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows19,text = "next",font = ('arial',12,'bold'),bg = '#008e76', command = bfourth_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows19.mainloop()


def bfourth_set_4():

   global windows20
   windows20 = Toplevel(windows19)
   windows20.title("Question 4")
   windows20.geometry("600x300+300+300")
   windows19.withdraw()

   lbl1 = Label(windows20,text = fourth_set_questions[3],font = ('arial',10,'bold'), bg='#00bfa5' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows20, text=fourth_set_answers_3[0], font = ('arial',10,'bold'), value=0, variable = v15, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows20, text=fourth_set_answers_3[1], font = ('arial',10,'bold'), value=1, variable = v15, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows20, text=fourth_set_answers_3[2], font = ('arial',10,'bold'), value=2, variable = v15, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows20, text=fourth_set_answers_3[3], font = ('arial',10,'bold'), value=3, variable = v15, indicator = 0, command = checked_fourth, bg = '#5df2d6')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows20,text = "back",font = ('arial',12,'bold'), bg='#5df2d6', command = bfrom20_to_19)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows20,text = "next",font = ('arial',12,'bold'),bg = '#008e76', command = bfourth_score)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows20.mainloop()

   

def bfourth_score():

   global windows21
   windows21 = Toplevel(windows20)
   windows21.title("Final Result")
   windows21.geometry("600x300+300+300")
   windows20.withdraw()
  
   lb_score = Label(windows21, text = "Your score is " + str(total_fourth) + "/4",font = ("arial",12,"bold"), bg='#ff1744')
   lb_score.pack(fill=X, ipady=15, side = TOP)
   lb_correct_answers = Label(windows21, text='The correct answers are: \ngit status \ngit branch \ngit checkout -b <branch> \ngit merge <branch>', font=('arial', 12, 'bold'), bg='#ff616f' )
   lb_correct_answers.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows21, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command=bfrom21_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows21, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows21.destroy)
   btn2.pack(side=RIGHT)

   windows21.mainloop()


# Fifth set
def bfifth_set():

   global windows22
   windows22 = Toplevel(root)
   windows22.title("Question 1")
   windows22.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows22, text = fifth_set_questions[0],font = ('arial',10,'bold'), bg='#00b8d4' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows22, text=fifth_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v16, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows22, text=fifth_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v16, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows22, text=fifth_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v16, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows22, text=fifth_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v16, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows22,text = "back",font = ('arial',12,'bold'), bg='#62ebff', command = bfrom22_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows22,text = "next",font = ('arial',12,'bold'),bg = '#0088a3', command = bfifth_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows22.mainloop()



# 5 - Question 2
def bfifth_set_2():

   global windows23
   windows23 = Toplevel(windows22)
   windows23.title("Question 2")
   windows23.geometry("600x300+300+300")
   windows22.withdraw()

   lbl1 = Label(windows23,text = fifth_set_questions[1],font = ('arial',10,'bold'), bg='#00b8d4' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows23, text=fifth_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v17, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows23, text=fifth_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v17, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows23, text=fifth_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v17, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows23, text=fifth_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v17, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows23,text = "back",font = ('arial',12,'bold'), bg='#62ebff', command = bfrom23_to_22)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows23,text = "next",font = ('arial',12,'bold'),bg = '#0088a3', command = bfifth_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows23.mainloop()



# 5 - Question 3

def bfifth_set_3():

   global windows24
   windows24 = Toplevel(windows23)
   windows24.title("Question 3")
   windows24.geometry("600x300+300+300")
   windows23.withdraw()

   lbl1 = Label(windows24, text = fifth_set_questions[2],font = ('arial',10,'bold'), bg='#00b8d4' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows24, text=fifth_set_answers_2[0], font = ('arial',10,'bold'), value=0, variable = v18, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows24, text=fifth_set_answers_2[1], font = ('arial',10,'bold'), value=1, variable = v18, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows24, text=fifth_set_answers_2[2], font = ('arial',10,'bold'), value=2, variable = v18, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows24, text=fifth_set_answers_2[3], font = ('arial',10,'bold'), value=3, variable = v18, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows24,text = "back",font = ('arial',12,'bold'), bg='#62ebff', command = bfrom24_to_23)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows24,text = "next",font = ('arial',12,'bold'),bg = '#0088a3', command = bfifth_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows24.mainloop()


# 5 - Question 4


def bfifth_set_4():

   global windows25
   windows25 = Toplevel(windows24)
   windows25.title("Question 4")
   windows25.geometry("600x300+300+300")
   windows24.withdraw()

   lbl1 = Label(windows25, text = fifth_set_questions[3],font = ('arial',10,'bold'), bg='#00b8d4' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows25, text=fifth_set_answers_3[0], font = ('arial',10,'bold'), value=0, variable = v19, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows25, text=fifth_set_answers_3[1], font = ('arial',10,'bold'), value=1, variable = v19, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows25, text=fifth_set_answers_3[2], font = ('arial',10,'bold'), value=2, variable = v19, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows25, text=fifth_set_answers_3[3], font = ('arial',10,'bold'), value=3, variable = v19, indicator = 0, command = checked_fifth, bg = '#62ebff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows25,text = "back",font = ('arial',12,'bold'), bg='#62ebff', command = bfrom24_to_23)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows25,text = "next",font = ('arial',12,'bold'),bg = '#0088a3', command = bfifth_score)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows24.mainloop()


# 5 -Score

def bfifth_score():

   global windows26
   windows26 = Toplevel(windows25)
   windows26.title("Final Result")
   windows26.geometry("600x300+300+300")
   windows25.withdraw()
  
   lb_score = Label(windows26, text = "Your score is " + str(total_fifth) + "/4",font = ("arial",12,"bold"), bg='#ff1744')
   lb_score.pack(fill=X, ipady=15, side = TOP)
   lb_correct_answers = Label(windows26, text='The correct answers are: \ngit remote add<name> <url> \ngit fetch<remote> <branch> \ngit pull <remote> \ngit push<remote> <branch>', font=('arial', 12, 'bold'), bg='#ff616f' )
   lb_correct_answers.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows26, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command=bfrom26_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows26, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows26.destroy)
   btn2.pack(side=RIGHT)

   windows26.mainloop()


#6 - Question 1

def bsixth_set():

   global windows27
   windows27 = Toplevel(root)
   windows27.title("Question 1")
   windows27.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows27,text = sixth_set_questions[0],font = ('arial',10,'bold'), bg='#0091ea' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows27, text=sixth_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v20, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows27, text=sixth_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v20, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows27, text=sixth_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v20, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows27, text=sixth_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v20, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows27, text = "back",font = ('arial',12,'bold'), bg='#64c1ff', command = bfrom27_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows27, text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#0064b7', command = bsixth_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows27.mainloop()   


# 6 - Question 2

def bsixth_set_2():

   global windows28
   windows28 = Toplevel(windows27)
   windows28.title("Question 2")
   windows28.geometry("600x300+300+300")
   windows27.withdraw()

   lbl1 = Label(windows28,text = sixth_set_questions[1],font = ('arial',10,'bold'), bg='#0091ea' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows28, text=sixth_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v21, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows28, text=sixth_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v21, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows28, text=sixth_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v21, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows28, text=sixth_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v21, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows28,text = "back",font = ('arial',12,'bold'), bg='#64c1ff', command = bfrom28_to_27)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows28,text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#0064b7', command = bsixth_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows28.mainloop()   



# 6 - Question 3

def bsixth_set_3():

   global windows29
   windows29 = Toplevel(windows28)
   windows29.title("Question 3")
   windows29.geometry("600x300+300+300")
   windows28.withdraw()

   lbl1 = Label(windows29, text = sixth_set_questions[2],font = ('arial',10,'bold'), bg='#0091ea' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows29, text=sixth_set_answers_2[0], font = ('arial',10,'bold'), value=0, variable = v22, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows29, text=sixth_set_answers_2[1], font = ('arial',10,'bold'), value=1, variable = v22, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows29, text=sixth_set_answers_2[2], font = ('arial',10,'bold'), value=2, variable = v22, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows29, text=sixth_set_answers_2[3], font = ('arial',10,'bold'), value=3, variable = v22, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows29,text = "back",font = ('arial',12,'bold'), bg='#64c1ff', command = bfrom29_to_28)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows29,text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#0064b7', command = bsixth_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows29.mainloop()   



# 6 - Question 4

def bsixth_set_4():

   global windows30
   windows30 = Toplevel(windows29)
   windows30.title("Question 4")
   windows30.geometry("600x300+300+300")
   windows29.withdraw()

   lbl1 = Label(windows30, text = sixth_set_questions[3],font = ('arial',10,'bold'), bg='#0091ea' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows30, text=sixth_set_answers_3[0], font = ('arial',10,'bold'), value=0, variable = v23, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows30, text=sixth_set_answers_3[1], font = ('arial',10,'bold'), value=1, variable = v23, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows30, text=sixth_set_answers_3[2], font = ('arial',10,'bold'), value=2, variable = v23, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows30, text=sixth_set_answers_3[3], font = ('arial',10,'bold'), value=3, variable = v23, indicator = 0, command = checked_sixth, bg = '#64c1ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows30, text = "back",font = ('arial',12,'bold'), bg='#64c1ff', command = bfrom30_to_29)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows30,text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#0064b7', command = bsixth_score)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows30.mainloop()   



# 6 - Score

def bsixth_score():

   global windows31
   windows31 = Toplevel(windows30)
   windows31.title("Final Result")
   windows31.geometry("600x300+300+300")
   windows30.withdraw()
  
   lb_score = Label(windows31, text = "Your score is " + str(total_sixth) + "/4",font = ("arial",12,"bold"), bg='#ff1744')
   lb_score.pack(fill=X, ipady=15, side = TOP)
   lb_correct_answers = Label(windows31, text='The correct answers are: \ngit config --global user.name <name> \ngit config --global user.email <email> \ngit config --systemcore.editor <editor> \ngit config --global --edit', font=('arial', 12, 'bold'), bg='#ff616f' )
   lb_correct_answers.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows31, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command=bfrom31_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows31, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows31.destroy)
   btn2.pack(side=RIGHT)

   windows31.mainloop()


# 7
# 7 - Question 1

def bseventh_set():

   global windows32
   windows32 = Toplevel(root)
   windows32.title("Question 1")
   windows32.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows32,text = seventh_set_questions[0],font = ('arial',10,'bold'), fg='#ffffff', bg='#2962ff' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows32, text=seventh_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v24, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows32, text=seventh_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v24, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows32, text=seventh_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v24, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows32, text=seventh_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v24, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows32, text = "back",font = ('arial',12,'bold'), bg='#768fff', command = bfrom32_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows32, text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#0039cb', command = bseventh_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows32.mainloop()  

# 7 - Question 2

def bseventh_set_2():

   global windows33
   windows33 = Toplevel(windows32)
   windows33.title("Question 2")
   windows33.geometry("600x300+300+300")
   windows32.withdraw()

   lbl1 = Label(windows33,text = seventh_set_questions[1],font = ('arial',10,'bold'), fg='#ffffff', bg='#2962ff' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows33, text=seventh_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v25, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows33, text=seventh_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v25, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows33, text=seventh_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v25, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows33, text=seventh_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v25, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows33, text = "back",font = ('arial',12,'bold'), bg='#768fff', command = bfrom33_to_32)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows33, text = "next", font = ('arial',12,'bold'), fg='#ffffff', bg = '#0039cb', command = bseventh_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows33.mainloop()  


# 7 - Question 3

def bseventh_set_3():

   global windows34
   windows34 = Toplevel(windows33)
   windows34.title("Question 3")
   windows34.geometry("600x300+300+300")
   windows33.withdraw()

   lbl1 = Label(windows34,text = seventh_set_questions[2],font = ('arial',10,'bold'), fg='#ffffff', bg='#2962ff' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows34, text=seventh_set_answers_2[0], font = ('arial',10,'bold'), value=0, variable = v26, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows34, text=seventh_set_answers_2[1], font = ('arial',10,'bold'), value=1, variable = v26, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows34, text=seventh_set_answers_2[2], font = ('arial',10,'bold'), value=2, variable = v26, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows34, text=seventh_set_answers_2[3], font = ('arial',10,'bold'), value=3, variable = v26, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows34, text = "back",font = ('arial',12,'bold'), bg='#768fff', command = bfrom34_to_33)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows34, text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#0039cb', command = bseventh_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows34.mainloop()  



# 7 - Question 4

def bseventh_set_4():

   global windows35
   windows35 = Toplevel(windows34)
   windows35.title("Question 3")
   windows35.geometry("600x300+300+300")
   windows34.withdraw()

   lbl1 = Label(windows35,text = seventh_set_questions[3],font = ('arial',10,'bold'), fg='#ffffff', bg='#2962ff' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows35, text=seventh_set_answers_3[0], font = ('arial',10,'bold'), value=0, variable = v27, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows35, text=seventh_set_answers_3[1], font = ('arial',10,'bold'), value=1, variable = v27, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows35, text=seventh_set_answers_3[2], font = ('arial',10,'bold'), value=2, variable = v27, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows35, text=seventh_set_answers_3[3], font = ('arial',10,'bold'), value=3, variable = v27, indicator = 0, command = checked_seventh, bg = '#768fff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows35, text = "back",font = ('arial',12,'bold'), bg='#768fff', command = bfrom33_to_32)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows35, text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#0039cb', command = bseventh_score)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows35.mainloop()  


# 7 - Score

def bseventh_score():

   global windows36
   windows36 = Toplevel(windows35)
   windows36.title("Final Result")
   windows36.geometry("600x300+300+300")
   windows35.withdraw()
  
   lb_score = Label(windows36, text = "Your score is " + str(total_seventh) + "/4",font = ("arial",12,"bold"), bg='#ff1744')
   lb_score.pack(fill=X, ipady=15, side = TOP)
   lb_correct_answers = Label(windows36, text='The correct answers are: \ngit log --oneline \ngit log -p \ngit log --author=”<pattern> \ngit log --graph --decorate', font=('arial', 12, 'bold'), bg='#ff616f' )
   lb_correct_answers.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows36, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command=bfrom36_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows36, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows36.destroy)
   btn2.pack(side=RIGHT)

   windows36.mainloop()



# 8
# 8 - Question 1
def beighth_set():

   global windows37
   windows37 = Toplevel(root)
   windows37.title("Question 1")
   windows37.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows37,text = eighth_set_questions[0],font = ('arial',10,'bold'), fg='#ffffff', bg='#304ffe' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows37, text=eighth_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v28, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows37, text=eighth_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v28, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows37, text=eighth_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v28, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows37, text=eighth_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v28, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows37,text = "back",font = ('arial',12,'bold'), bg='#7a7cff', command = bfrom37_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows37,text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#0026ca', command = beighth_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows37.mainloop()   


#8 - Question 2

def beighth_set_2():

   global windows38
   windows38 = Toplevel(windows37)
   windows38.title("Question 2")
   windows38.geometry("600x300+300+300")
   windows37.withdraw()

   lbl1 = Label(windows38,text = eighth_set_questions[1],font = ('arial',10,'bold'), fg='#ffffff', bg='#304ffe' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows38, text=eighth_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v29, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows38, text=eighth_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v29, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows38, text=eighth_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v29, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows38, text=eighth_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v29, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows38,text = "back",font = ('arial',12,'bold'), bg='#7a7cff', command = bfrom38_to_37)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows38, text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#0026ca', command = beighth_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows38.mainloop()   


# 8 - Question 3

def beighth_set_3():

   global windows39
   windows39 = Toplevel(windows38)
   windows39.title("Question 3")
   windows39.geometry("600x300+300+300")
   windows38.withdraw()

   lbl1 = Label(windows39,text = eighth_set_questions[2],font = ('arial',10,'bold'), fg='#ffffff', bg='#304ffe' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows39, text=eighth_set_answers_2[0], font = ('arial',10,'bold'), value=0, variable = v30, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows39, text=eighth_set_answers_2[1], font = ('arial',10,'bold'), value=1, variable = v30, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows39, text=eighth_set_answers_2[2], font = ('arial',10,'bold'), value=2, variable = v30, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows39, text=eighth_set_answers_2[3], font = ('arial',10,'bold'), value=3, variable = v30, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows39,text = "back",font = ('arial',12,'bold'), bg='#7a7cff', command = bfrom39_to_38)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows39, text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#0026ca', command = beighth_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows39.mainloop()   


# 8 - Question 4


def beighth_set_4():

   global windows40
   windows40 = Toplevel(windows39)
   windows40.title("Question 3")
   windows40.geometry("600x300+300+300")
   windows39.withdraw()

   lbl1 = Label(windows40,text = eighth_set_questions[3],font = ('arial',10,'bold'), fg='#ffffff', bg='#304ffe' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows40, text=eighth_set_answers_3[0], font = ('arial',10,'bold'), value=0, variable = v31, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows40, text=eighth_set_answers_3[1], font = ('arial',10,'bold'), value=1, variable = v31, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows40, text=eighth_set_answers_3[2], font = ('arial',10,'bold'), value=2, variable = v31, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows40, text=eighth_set_answers_3[3], font = ('arial',10,'bold'), value=3, variable = v31, indicator = 0, command = checked_eighth, bg = '#7a7cff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows40,text = "back",font = ('arial',12,'bold'), bg='#7a7cff', command = bfrom40_to_39)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows40, text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#0026ca', command = beighth_score)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows40.mainloop()


# 8 - Score

def beighth_score():

   global windows41
   windows41 = Toplevel(windows40)
   windows41.title("Final Result")
   windows41.geometry("600x300+300+300")
   windows40.withdraw()
  
   lb_score = Label(windows41, text = "Your score is " + str(total_eighth) + "/4",font = ("arial",12,"bold"), bg='#ff1744')
   lb_score.pack(fill=X, ipady=15, side = TOP)
   lb_correct_answers = Label(windows41, text='The correct answers are: \ngit diff HEAD \n git diff --cached \ngit diff --color-words \ngit diff-highlight', font=('arial', 12, 'bold'), bg='#ff616f' )
   lb_correct_answers.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows41, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command=bfrom41_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows41, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows41.destroy)
   btn2.pack(side=RIGHT)

   windows41.mainloop()


# 9
# 9 - Question 1

def bninth_set():

   global windows42
   windows42 = Toplevel(root)
   windows42.title("Question 1")
   windows42.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows42, text = ninth_set_questions[0],font = ('arial',10,'bold'), fg='#ffffff', bg='#6200ea' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows42, text=ninth_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v32, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows42, text=ninth_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v32, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows42, text=ninth_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v32, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows42, text=ninth_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v32, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows42, text = "back", font = ('arial',12,'bold'), bg='#9d46ff', command = bfrom42_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows42, text = "next", font = ('arial',12,'bold'), fg='#ffffff', bg = '#0a00b6', command = bninth_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows42.mainloop()


# 9 - Question 2

def bninth_set_2():

   global windows43
   windows43 = Toplevel(windows42)
   windows43.title("Question 2")
   windows43.geometry("600x300+300+300")
   windows42.withdraw()

   lbl1 = Label(windows43, text = ninth_set_questions[1], font = ('arial',10,'bold'), fg='#ffffff', bg='#6200ea' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows43, text=ninth_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v33, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows43, text=ninth_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v33, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows43, text=ninth_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v33, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows43, text=ninth_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v33, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows43, text = "back", font = ('arial',12,'bold'), bg='#9d46ff', command = bfrom43_to_42)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows43, text = "next", font = ('arial',12,'bold'), fg='#ffffff', bg = '#0a00b6', command = bninth_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows43.mainloop()


# 9 - Question 3

def bninth_set_3():

   global windows44
   windows44 = Toplevel(windows43)
   windows44.title("Question 3")
   windows44.geometry("600x300+300+300")
   windows43.withdraw()

   lbl1 = Label(windows44, text = ninth_set_questions[2], font = ('arial',10,'bold'), fg='#ffffff', bg='#6200ea' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows44, text=ninth_set_answers_2[0], font = ('arial',10,'bold'), value=0, variable = v34, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows44, text=ninth_set_answers_2[1], font = ('arial',10,'bold'), value=1, variable = v34, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows44, text=ninth_set_answers_2[2], font = ('arial',10,'bold'), value=2, variable = v34, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows44, text=ninth_set_answers_2[3], font = ('arial',10,'bold'), value=3, variable = v34, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows44, text = "back", font = ('arial',12,'bold'), bg='#9d46ff', command = bfrom44_to_43)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows44, text = "next", font = ('arial',12,'bold'), fg='#ffffff', bg = '#0a00b6', command = bninth_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows44.mainloop()


# 9 - Question 4


def bninth_set_4():

   global windows45
   windows45 = Toplevel(windows44)
   windows45.title("Question 4")
   windows45.geometry("600x300+300+300")
   windows44.withdraw()

   lbl1 = Label(windows45, text = ninth_set_questions[3], font = ('arial',10,'bold'), fg='#ffffff', bg='#6200ea' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows45, text=ninth_set_answers_3[0], font = ('arial',10,'bold'), value=0, variable = v35, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows45, text=ninth_set_answers_3[1], font = ('arial',10,'bold'), value=1, variable = v35, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows45, text=ninth_set_answers_3[2], font = ('arial',10,'bold'), value=2, variable = v35, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows45, text=ninth_set_answers_3[3], font = ('arial',10,'bold'), value=3, variable = v35, indicator = 0, command = checked_ninth, bg = '#9d46ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows45, text = "back", font = ('arial',12,'bold'), bg='#9d46ff', command = bfrom45_to_44)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows45, text = "next", font = ('arial',12,'bold'), fg='#ffffff', bg = '#0a00b6', command = bninth_score)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows45.mainloop()


# 9 - Score

def bninth_score():

   global windows46
   windows46 = Toplevel(windows45)
   windows46.title("Final Result")
   windows46.geometry("600x300+300+300")
   windows45.withdraw()
  
   lb_score = Label(windows46, text = "Your score is " + str(total_ninth) + "/4",font = ("arial",12,"bold"), bg='#ff1744')
   lb_score.pack(fill=X, ipady=15, side = TOP)
   lb_correct_answers = Label(windows46, text='The correct answers are: \ngit reset \ngit reset --hard \ngit reset <commit> \ngit reset --hard <commit>', font=('arial', 12, 'bold'), bg='#ff616f' )
   lb_correct_answers.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows46, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command=bfrom46_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows46, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows46.destroy)
   btn2.pack(side=RIGHT)

   windows46.mainloop()


# 10
#10 - Question 1

def btenth_set():

   global windows47
   windows47 = Toplevel(root)
   windows47.title("Question 1")
   windows47.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows47,text = tenth_set_questions[0],font = ('arial',10,'bold'), fg='#ffffff', bg='#aa00ff' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows47, text=tenth_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v36, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows47, text=tenth_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v36, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows47, text=tenth_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v36, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows47, text=tenth_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v36, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows47,text = "back",font = ('arial',12,'bold'), bg='#e254ff', command = bfrom47_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows47,text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#7200ca', command = btenth_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows47.mainloop()


# 10 - Question 2

def btenth_set_2():

   global windows48
   windows48 = Toplevel(windows47)
   windows48.title("Question 2")
   windows48.geometry("600x300+300+300")
   windows47.withdraw()

   lbl1 = Label(windows48, text = tenth_set_questions[1],font = ('arial',10,'bold'), fg='#ffffff', bg='#aa00ff' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows48, text=tenth_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v37, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows48, text=tenth_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v37, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows48, text=tenth_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v37, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows48, text=tenth_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v37, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows48, text = "back",font = ('arial',12,'bold'), bg='#e254ff', command = bfrom48_to_47)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows48, text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#7200ca', command = btenth_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows48.mainloop()


# 10 - Question 3

def btenth_set_3():

   global windows49
   windows49 = Toplevel(windows48)
   windows49.title("Question 3")
   windows49.geometry("600x300+300+300")
   windows48.withdraw()

   lbl1 = Label(windows49, text = tenth_set_questions[2],font = ('arial',10,'bold'), fg='#ffffff', bg='#aa00ff' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows49, text=tenth_set_answers_2[0], font = ('arial',10,'bold'), value=0, variable = v38, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows49, text=tenth_set_answers_2[1], font = ('arial',10,'bold'), value=1, variable = v38, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows49, text=tenth_set_answers_2[2], font = ('arial',10,'bold'), value=2, variable = v38, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows49, text=tenth_set_answers_2[3], font = ('arial',10,'bold'), value=3, variable = v38, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows49, text = "back",font = ('arial',12,'bold'), bg='#e254ff', command = bfrom49_to_48)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows49, text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#7200ca', command = btenth_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows49.mainloop()


# 10 - Question 4

def btenth_set_4():

   global windows50
   windows50 = Toplevel(windows49)
   windows50.title("Question 4")
   windows50.geometry("600x300+300+300")
   windows49.withdraw()

   lbl1 = Label(windows50, text = tenth_set_questions[3],font = ('arial',10,'bold'), fg='#ffffff', bg='#aa00ff' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows50, text=tenth_set_answers_3[0], font = ('arial',10,'bold'), value=0, variable = v39, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows50, text=tenth_set_answers_3[1], font = ('arial',10,'bold'), value=1, variable = v39, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows50, text=tenth_set_answers_3[2], font = ('arial',10,'bold'), value=2, variable = v39, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows50, text=tenth_set_answers_3[3], font = ('arial',10,'bold'), value=3, variable = v39, indicator = 0, command = checked_tenth, bg = '#e254ff')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows50, text = "back",font = ('arial',12,'bold'), bg='#e254ff', command = bfrom50_to_49)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows50, text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#7200ca', command = btenth_score)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows50.mainloop()


# 10 - Score

def btenth_score():

   global windows51
   windows51 = Toplevel(windows50)
   windows51.title("Final Result")
   windows51.geometry("600x300+300+300")
   windows50.withdraw()
  
   lb_score = Label(windows51, text = "Your score is " + str(total_tenth) + "/4",font = ("arial",12,"bold"), bg='#ff1744')
   lb_score.pack(fill=X, ipady=15, side = TOP)
   lb_correct_answers = Label(windows51, text='The correct answers are: \ngit rebase -i<base> \npick \n squash \n drop ', font=('arial', 12, 'bold'), bg='#ff616f' )
   lb_correct_answers.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows51, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command=bfrom51_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows51, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows51.destroy)
   btn2.pack(side=RIGHT)

   windows51.mainloop()


# 11
# 11- Question 1

def beleventh_set():

   global windows52
   windows52 = Toplevel(root)
   windows52.title("Question 1")
   windows52.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows52, text = eleventh_set_questions[0],font = ('arial',10,'bold'), fg="#ffffff", bg='#c51162' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows52, text=eleventh_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v40, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows52, text=eleventh_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v40, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows52, text=eleventh_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v40, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows52, text=eleventh_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v40, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows52, text = "back",font = ('arial',12,'bold'), bg='#fd558f', command = bfrom52_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows52, text = "next",font = ('arial',12,'bold'), fg="#ffffff", bg = '#8e0038', command = beleventh_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows52.mainloop()


# 11 -Question 2

def beleventh_set_2():

   global windows53
   windows53 = Toplevel(windows52)
   windows53.title("Question 2")
   windows53.geometry("600x300+300+300")
   windows52.withdraw()

   lbl1 = Label(windows53, text = eleventh_set_questions[1],font = ('arial',10,'bold'), fg="#ffffff", bg='#c51162' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows53, text=eleventh_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v41, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows53, text=eleventh_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v41, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows53, text=eleventh_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v41, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows53, text=eleventh_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v41, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows53, text = "back",font = ('arial',12,'bold'), bg='#fd558f', command = bfrom53_to_52)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows53, text = "next",font = ('arial',12,'bold'),fg="#ffffff", bg = '#8e0038', command = beleventh_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows53.mainloop()


# 11 -  Question 3

def beleventh_set_3():

   global windows54
   windows54 = Toplevel(windows53)
   windows54.title("Question 3")
   windows54.geometry("600x300+300+300")
   windows53.withdraw()

   lbl1 = Label(windows54, text = eleventh_set_questions[2], font = ('arial',10,'bold'), fg="#ffffff", bg='#c51162' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows54, text=eleventh_set_answers_2[0], font = ('arial',10,'bold'), value=0, variable = v42, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows54, text=eleventh_set_answers_2[1], font = ('arial',10,'bold'), value=1, variable = v42, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows54, text=eleventh_set_answers_2[2], font = ('arial',10,'bold'), value=2, variable = v42, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows54, text=eleventh_set_answers_2[3], font = ('arial',10,'bold'), value=3, variable = v42, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows54, text = "back",font = ('arial',12,'bold'), bg='#fd558f', command = bfrom54_to_53)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows54, text = "next",font = ('arial',12,'bold'), fg="#ffffff", bg = '#8e0038', command = beleventh_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows54.mainloop()


# 11 - Question 4

def beleventh_set_4():

   global windows55
   windows55 = Toplevel(windows54)
   windows55.title("Question 4")
   windows55.geometry("600x300+300+300")
   windows54.withdraw()

   lbl1 = Label(windows55, text = eleventh_set_questions[3], font = ('arial',10,'bold'), fg="#ffffff", bg='#c51162' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows55, text=eleventh_set_answers_3[0], font = ('arial',10,'bold'), value=0, variable = v43, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows55, text=eleventh_set_answers_3[1], font = ('arial',10,'bold'), value=1, variable = v43, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows55, text=eleventh_set_answers_3[2], font = ('arial',10,'bold'), value=2, variable = v43, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows55, text=eleventh_set_answers_3[3], font = ('arial',10,'bold'), value=3, variable = v43, indicator = 0, command = checked_eleventh, bg = '#fd558f')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows55, text = "back",font = ('arial',12,'bold'), bg='#fd558f', command = bfrom55_to_54)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows55, text = "next",font = ('arial',12,'bold'), fg="#ffffff", bg = '#8e0038', command = beleventh_score)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows55.mainloop()


# 11 - Score

def beleventh_score():

   global windows56
   windows56 = Toplevel(windows55)
   windows56.title("Final Result")
   windows56.geometry("600x300+300+300")
   windows55.withdraw()
  
   lb_score = Label(windows56, text = "Your score is " + str(total_eleventh) + "/4",font = ("arial",12,"bold"), bg='#ff1744')
   lb_score.pack(fill=X, ipady=15, side = TOP)
   lb_correct_answers = Label(windows56, text='The correct answers are: \ngit pull --no-commit \ngit pull --verbose \ngit pull --rebase \ngit pull --rebase <remote> ', font=('arial', 12, 'bold'), bg='#ff616f' )
   lb_correct_answers.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows56, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command=bfrom56_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows56, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows56.destroy)
   btn2.pack(side=RIGHT)

   windows56.mainloop()



# 12
# 12 - Question 1

def btwelfth_set():

   global windows57
   windows57 = Toplevel(root)
   windows57.title("Question 1")
   windows57.geometry("600x300+300+300")
   root.withdraw()

   lbl1 = Label(windows57,text = twelfth_set_questions[0],font = ('arial',10,'bold'), fg='#ffffff', bg='#d50000' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows57, text=twelfth_set_answers_0[0], font = ('arial',10,'bold'), value=0, variable = v44, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows57, text=twelfth_set_answers_0[1], font = ('arial',10,'bold'), value=1, variable = v44, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows57, text=twelfth_set_answers_0[2], font = ('arial',10,'bold'), value=2, variable = v44, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows57, text=twelfth_set_answers_0[3], font = ('arial',10,'bold'), value=3, variable = v44, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows57,text = "back",font = ('arial',12,'bold'), bg='#ff5131', command = bfrom57_to_menu)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows57,text = "next",font = ('arial',12,'bold'), fg='#ffffff', bg = '#9b0000', command = btwelfth_set_2)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows57.mainloop()


# 12 - Question 2

def btwelfth_set_2():

   global windows58
   windows58 = Toplevel(windows57)
   windows58.title("Question 2")
   windows58.geometry("600x300+300+300")
   windows57.withdraw()

   lbl1 = Label(windows58,  text = twelfth_set_questions[1],font = ('arial',10,'bold'), fg='#ffffff', bg='#d50000' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows58, text=twelfth_set_answers_1[0], font = ('arial',10,'bold'), value=0, variable = v45, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows58, text=twelfth_set_answers_1[1], font = ('arial',10,'bold'), value=1, variable = v45, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows58, text=twelfth_set_answers_1[2], font = ('arial',10,'bold'), value=2, variable = v45, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows58, text=twelfth_set_answers_1[3], font = ('arial',10,'bold'), value=3, variable = v45, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows58, text = "back", font = ('arial',12,'bold'), bg='#ff5131', command = bfrom58_to_57)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows58, text = "next", font = ('arial',12,'bold'), fg='#ffffff', bg = '#9b0000', command = btwelfth_set_3)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows58.mainloop()


# 12 - Question 3


def btwelfth_set_3():

   global windows59
   windows59 = Toplevel(windows58)
   windows59.title("Question 3")
   windows59.geometry("600x300+300+300")
   windows58.withdraw()

   lbl1 = Label(windows59,  text = twelfth_set_questions[2],font = ('arial',10,'bold'), fg='#ffffff', bg='#d50000' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows59, text=twelfth_set_answers_2[0], font = ('arial',10,'bold'), value=0, variable = v46, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows59, text=twelfth_set_answers_2[1], font = ('arial',10,'bold'), value=1, variable = v46, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows59, text=twelfth_set_answers_2[2], font = ('arial',10,'bold'), value=2, variable = v46, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows59, text=twelfth_set_answers_2[3], font = ('arial',10,'bold'), value=3, variable = v46, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows59, text = "back", font = ('arial',12,'bold'), bg='#ff5131', command = bfrom59_to_58)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows59, text = "next", font = ('arial',12,'bold'), fg='#ffffff', bg = '#9b0000', command = btwelfth_set_4)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows59.mainloop()


# 12 - Question 4


def btwelfth_set_4():

   global windows60
   windows60 = Toplevel(windows59)
   windows60.title("Question 3")
   windows60.geometry("600x300+300+300")
   windows59.withdraw()

   lbl1 = Label(windows60,  text = twelfth_set_questions[3],font = ('arial',10,'bold'), fg='#ffffff', bg='#d50000' )
   lbl1.pack(fill=X, ipady=15, side = TOP)
   rb1 = Radiobutton(windows60, text=twelfth_set_answers_3[0], font = ('arial',10,'bold'), value=0, variable = v47, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb1.pack(fill=X, ipady=5, side=TOP)
   rb2 = Radiobutton(windows60, text=twelfth_set_answers_3[1], font = ('arial',10,'bold'), value=1, variable = v47, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb2.pack(fill=X, ipady=5, side=TOP)
   rb3 = Radiobutton(windows60, text=twelfth_set_answers_3[2], font = ('arial',10,'bold'), value=2, variable = v47, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb3.pack(fill=X, ipady=5, side=TOP)
   rb4 = Radiobutton(windows60, text=twelfth_set_answers_3[3], font = ('arial',10,'bold'), value=3, variable = v47, indicator = 0, command = checked_twelfth, bg = '#ff5131')
   rb4.pack(fill=X, ipady=5, side=TOP)
   btn1 = Button(windows60, text = "back", font = ('arial',12,'bold'), bg='#ff5131', command = bfrom60_to_59)
   btn1.pack(padx=15, ipady=5, side=LEFT)
   btn2 = Button(windows60, text = "next" ,font = ('arial',12,'bold'), fg='#ffffff', bg = '#9b0000', command = btwelfth_score)
   btn2.pack(padx=15, ipady=5, side=RIGHT)
   windows60.mainloop()


# 12 - Score

def btwelfth_score():

   global windows61
   windows61 = Toplevel(windows60)
   windows61.title("Final Result")
   windows61.geometry("600x300+300+300")
   windows60.withdraw()
  
   lb_score = Label(windows61, text = "Your score is " + str(total_twelfth) + "/4",font = ("arial",12,"bold"), bg='#ff1744')
   lb_score.pack(fill=X, ipady=15, side = TOP)
   lb_correct_answers = Label(windows61, text='The correct answers are: \ngit push <remote> --force \ngit push <remote> --all \n git push <remote> --tags \ngit push -u ', font=('arial', 12, 'bold'), bg='#ff616f' )
   lb_correct_answers.pack(fill=X, ipady=15, side = TOP)
   btn1 = Button(windows61, text="back to menu", font=('arial', 12, 'bold'), bg='#FF0266', fg='#ffffff', command=bfrom61_to_menu)
   btn1.pack(side=LEFT)
   btn2 = Button(windows61, text="Quit", font=('arial', 12, 'bold'),
                  bg='#c4001d', fg='#ffffff', command=windows61.destroy)
   btn2.pack(side=RIGHT)

   windows61.mainloop()




# Going back

def bback_to_menu():

    windows.withdraw()
    root.deiconify()
    root.mainloop()


def bfrom3_to_1():
    
    windows3.withdraw()
    windows.deiconify()
    windows.mainloop()


def bfrom4_to_3():

    windows4.withdraw()
    windows3.deiconify()
    windows3.mainloop()


def bfrom5_to_4():

    windows5.withdraw()
    windows4.deiconify()
    windows4.mainloop()


def bfrom6_to_menu():

    windows6.withdraw()
    root.deiconify()
    root.mainloop()
    

def bfrom7_to_menu():
   
   windows7.withdraw()
   root.deiconify()
   root.mainloop()

   
def bfrom8_to_7():
   
   windows8.withdraw()
   windows7.deiconify()
   windows7.mainloop()


def bfrom9_to_8():
   
   windows9.withdraw()
   windows8.deiconify()
   windows8.mainloop()


def bfrom10_to_9():
   
   windows10.withdraw()
   windows9.deiconify()
   windows9.mainloop()    
    

def bfrom11_to_menu():

    windows11.withdraw()
    root.deiconify()
    root.mainloop()



def bfrom12_to_menu():
   
   windows12.withdraw()
   root.deiconify()
   root.mainloop()
    

def bfrom13_to_12():
   
   windows13.withdraw()
   windows12.deiconify()
   windows12.mainloop()


def bfrom14_to_13():
   
   windows14.withdraw()
   windows13.deiconify()
   windows13.mainloop()


def bfrom15_to_14():
   
   windows15.withdraw()
   windows14.deiconify()
   windows14.mainloop()


def bfrom16_to_menu():

    windows16.withdraw()
    root.deiconify()
    root.mainloop()
   

def bfrom17_to_menu():

    windows17.withdraw()
    root.deiconify()
    root.mainloop()


def bfrom18_to_17():

   windows18.withdraw()
   windows17.deiconify()
   windows17.mainloop()


def bfrom19_to_18():

   windows19.withdraw()
   windows18.deiconify()
   windows18.mainloop()
   

def bfrom20_to_19():

   windows20.withdraw()
   windows19.deiconify()
   windows19.mainloop()


def bfrom21_to_menu():

   windows21.withdraw()
   root.deiconify()
   root.mainloop()
    

def bfrom22_to_menu():

   windows22.withdraw()
   root.deiconify()
   root.mainloop()   


def bfrom23_to_22():

   windows23.withdraw()
   windows22.deiconify()
   windows22.mainloop()   



def bfrom24_to_23():

   windows24.withdraw()
   windows23.deiconify()
   windows23.mainloop()



def bfrom25_to_24():

   windows25.withdraw()
   windows24.deiconify()
   windows24.mainloop()   


def bfrom26_to_menu():

   windows26.withdraw()
   root.deiconify()
   root.mainloop()     


def bfrom27_to_menu():

   windows27.withdraw()
   root.deiconify()
   root.mainloop()


def bfrom28_to_27():

   windows28.withdraw()
   windows27.deiconify()
   windows27.mainloop()     


def bfrom29_to_28():

   windows29.withdraw()
   windows28.deiconify()
   windows28.mainloop()     



def bfrom30_to_29():

   windows30.withdraw()
   windows29.deiconify()
   windows29.mainloop()     



def bfrom31_to_menu():
   
   windows31.withdraw()
   root.deiconify()
   root.mainloop()

   
def bfrom32_to_menu():

   windows32.withdraw()
   root.deiconify()
   root.mainloop()      


def bfrom33_to_32():

   windows33.withdraw()
   windows32.deiconify()
   windows32.mainloop()     


def bfrom34_to_33():

   windows34.withdraw()
   windows33.deiconify()
   windows33.mainloop()     


def bfrom35_to_34():

   windows35.withdraw()
   windows34.deiconify()
   windows34.mainloop()     



def bfrom36_to_menu():

   windows36.withdraw()
   root.deiconify()
   root.mainloop()


def bfrom37_to_menu():

   windows37.withdraw()
   root.deiconify()
   root.mainloop()      


def bfrom38_to_37():

   windows38.withdraw()
   windows37.deiconify()
   windows37.mainloop()     


def bfrom39_to_38():

   windows39.withdraw()
   windows38.deiconify()
   windows38.mainloop()     



def bfrom40_to_39():

   windows40.withdraw()
   windows39.deiconify()
   windows39.mainloop()     


def bfrom41_to_menu():

   windows41.withdraw()
   root.deiconify()
   root.mainloop()      


def bfrom42_to_menu():

   windows42.withdraw()
   root.deiconify()
   root.mainloop()      


def bfrom43_to_42():

   windows43.withdraw()
   windows42.deiconify()
   windows42.mainloop()


def bfrom44_to_43():

   windows44.withdraw()
   windows43.deiconify()
   windows43.mainloop()        


def bfrom45_to_44():

   windows45.withdraw()
   windows44.deiconify()
   windows44.mainloop()     



def bfrom46_to_menu():

   windows46.withdraw()
   root.deiconify()
   root.mainloop()      


def bfrom47_to_menu():

   windows47.withdraw()
   root.deiconify()
   root.mainloop()      


def bfrom48_to_47():

   windows48.withdraw()
   windows47.deiconify()
   windows47.mainloop()     


def bfrom49_to_48():

   windows49.withdraw()
   windows48.deiconify()
   windows48.mainloop()


def bfrom50_to_49():

   windows50.withdraw()
   windows49.deiconify()
   windows49.mainloop()     
   

def bfrom51_to_menu():
   
   windows51.withdraw()
   root.deiconify()
   root.mainloop()


def bfrom52_to_menu():

   windows52.withdraw()
   root.deiconify()
   root.mainloop()


def bfrom53_to_52():

   windows53.withdraw()
   windows52.deiconify()
   windows52.mainloop()     



def bfrom54_to_53():

   windows54.withdraw()
   windows53.deiconify()
   windows53.mainloop()     


def bfrom55_to_54():

   windows55.withdraw()
   windows54.deiconify()
   windows54.mainloop()     


def bfrom56_to_menu():

   windows56.withdraw()
   root.deiconify()
   root.mainloop()


def bfrom57_to_menu():

   windows57.withdraw()
   root.deiconify()
   root.mainloop()



def bfrom58_to_57():

   windows58.withdraw()
   windows57.deiconify()
   windows57.mainloop()     


def bfrom59_to_58():

   windows59.withdraw()
   windows58.deiconify()
   windows58.mainloop()


def bfrom60_to_59():

   windows60.withdraw()
   windows59.deiconify()
   windows59.mainloop()        


def bfrom61_to_menu():

   windows61.withdraw()
   root.deiconify()
   root.mainloop()


# Counting score per sets

def checked():

    c = 0
    if v0.get() == 2:

        c += 1

    if v1.get() == 3:

        c += 1

    if v2.get() == 1:

        c += 1

    if v3.get() == 2:

        c += 1

    global total
    total = c


def checked_second():

    c_second = 0
    if v4.get() == 0:

        c_second += 1

    if v5.get() == 2:

        c_second += 1

    if v6.get() == 1:

        c_second += 1

    if v7.get() == 3:

        c_second += 1

    global total_second
    total_second = c_second


def checked_third():

    c_third = 0
    if v8.get() == 2:

        c_third += 1

    if v9.get() == 0:

        c_third += 1

    if v10.get() == 1:

        c_third += 1

    if v11.get() == 3:

        c_third += 1

    global total_third
    total_third = c_third


def checked_fourth():

    c_fourth = 0
    if v12.get() == 1:

        c_fourth += 1

    if v13.get() == 2:

        c_fourth += 1

    if v14.get() == 0:

        c_fourth += 1

    if v15.get() == 1:

        c_fourth += 1

    global total_fourth
    total_fourth = c_fourth


def checked_fifth():

    c_fifth = 0
    if v16.get() == 0:

        c_fifth += 1

    if v17.get() == 2:

        c_fifth += 1

    if v18.get() == 1:

        c_fifth += 1

    if v19.get() == 3:

        c_fifth += 1

    global total_fifth
    total_fifth = c_fifth


def checked_sixth():

    c_sixth = 0
    if v20.get() == 2:

        c_sixth += 1

    if v21.get() == 0:

        c_sixth += 1

    if v22.get() == 1:

        c_sixth += 1

    if v23.get() == 3:

        c_sixth += 1

    global total_sixth
    total_sixth = c_sixth



def checked_seventh():

    c_seventh = 0
    if v24.get() == 1:

        c_seventh += 1

    if v25.get() == 2:

        c_seventh += 1

    if v26.get() == 0:

        c_seventh += 1

    if v27.get() == 1:

        c_seventh += 1

    global total_seventh
    total_seventh = c_seventh



def checked_eighth():

    c_eighth = 0
    if v28.get() == 0:

        c_eighth += 1

    if v29.get() == 2:

        c_eighth += 1

    if v30.get() == 1:

        c_eighth += 1

    if v31.get() == 3:

        c_eighth += 1

    global total_eighth
    total_eighth = c_eighth



def checked_ninth():

    c_ninth = 0
    if v32.get() == 2:

        c_ninth += 1

    if v33.get() == 0:

        c_ninth += 1

    if v34.get() == 1:

        c_ninth += 1

    if v35.get() == 3:

        c_ninth += 1

    global total_ninth
    total_ninth = c_ninth



def checked_tenth():

    c_tenth = 0
    if v36.get() == 1:

        c_tenth += 1

    if v37.get() == 2:

        c_tenth += 1

    if v38.get() == 0:

        c_tenth += 1

    if v39.get() == 1:

        c_tenth += 1

    global total_tenth
    total_tenth = c_tenth



def checked_eleventh():

    c_eleventh = 0
    if v40.get() == 0:

        c_eleventh += 1

    if v41.get() == 2:

        c_eleventh += 1

    if v42.get() == 1:

        c_eleventh += 1

    if v43.get() == 3:

        c_eleventh += 1

    global total_eleventh
    total_eleventh = c_eleventh



def checked_twelfth():

    c_twelfth = 0
    if v44.get() == 2:

        c_twelfth += 1

    if v45.get() == 0:

        c_twelfth += 1

    if v46.get() == 1:

        c_twelfth += 1

    if v47.get() == 3:

        c_twelfth += 1

    global total_twelfth
    total_twelfth = c_twelfth



root = Tk()

v0 = IntVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()

v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
v7 = IntVar()

v8 = IntVar()
v9 = IntVar()
v10 = IntVar()
v11 = IntVar()

v12 = IntVar()
v13 = IntVar()
v14 = IntVar()
v15 = IntVar()

v16 = IntVar()
v17 = IntVar()
v18 = IntVar()
v19 = IntVar()

v20 = IntVar()
v21 = IntVar()
v22 = IntVar()
v23 = IntVar()

v24 = IntVar()
v25 = IntVar()
v26 = IntVar()
v27 = IntVar()

v28 = IntVar()
v29 = IntVar()
v30 = IntVar()
v31 = IntVar()

v32 = IntVar()
v33 = IntVar()
v34 = IntVar()
v35 = IntVar()

v36 = IntVar()
v37 = IntVar()
v38 = IntVar()
v39 = IntVar()

v40 = IntVar()
v41 = IntVar()
v42 = IntVar()
v43 = IntVar()

v44 = IntVar()
v45 = IntVar()
v46 = IntVar()
v47 = IntVar()

root.title("Quiz")
# window width * window height + position right + position down
root.geometry("500x580+300+300")

lbl_title = Label(root, text = "Test your knowledge of Git", font = ('arial', 20, 'bold'), bg='#ffd600')
lbl_title.pack(fill=X, ipady=20, side = TOP)

btn0 = Button(root, text = "Git basics                   ", font = ('arial',15,'bold'), command = bfirst_set, bg = '#aeea00')
btn0.pack(fill=X, side = TOP)

btn1 = Button(root, text = "Undoing changes       ", font = ('arial',15,'bold'), command = bsecond_set,  bg = '#64dd17')
btn1.pack(fill=X, side = TOP)

btn2= Button(root, text = "Rewriting Git history  ", font = ('arial',15,'bold'), command = bthird_set, bg = '#00c853')
btn2.pack(fill=X, side = TOP)

btn3= Button(root, text = "Git branches               ", font = ('arial',15,'bold'), command = bfourth_set, bg = '#00bfa5')
btn3.pack(fill=X, side = TOP)

btn4= Button(root, text = "Remote repositories   ", font = ('arial',15,'bold'), command = bfifth_set, bg = '#00b8d4')
btn4.pack(fill=X, side = TOP)

btn5= Button(root, text = "Git config                    ", font = ('arial',15,'bold'), command = bsixth_set, bg = '#0091ea')
btn5.pack(fill=X, side = TOP)

btn6= Button(root, text = "Git log                         ", font = ('arial',15,'bold'), command = bseventh_set, bg = '#2962ff')
btn6.pack(fill=X, side = TOP)

btn7= Button(root, text = "Git diff                         ", font = ('arial',15,'bold'), command = beighth_set, bg = '#304ffe')
btn7.pack(fill=X, side = TOP)

btn8= Button(root, text = "Git reset                      ", font = ('arial',15,'bold'), command = bninth_set, bg = '#6200ea')
btn8.pack(fill=X, side = TOP)

btn9= Button(root, text = "Git rebase                   ", font = ('arial',15,'bold'), command = btenth_set, bg = '#aa00ff')
btn9.pack(fill=X, side = TOP)

btn10= Button(root, text = "Git pull                        ", font = ('arial',15,'bold'), command = beleventh_set, bg = '#c51162')
btn10.pack(fill=X, side = TOP)

btn11= Button(root, text = "Git push                       ", font = ('arial',15,'bold'), command = btwelfth_set, bg = '#d50000')
btn11.pack(fill=X, side = TOP)


root.mainloop()

