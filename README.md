# HW0: Environment setup for EECS 331 @ NU

In this initial assignment, the goals are:

1. to set up a working programming environment using either conda environments.
2. to get acclimated to the "pull, commit, push" development cycle for git. This course's programming assignments will be submitted via Github (all free-response questions will be submitted via Canvas).
3. to get acclimated with Jupyter Lab, which is required for all assignments in this course.
4. to get familiar with Latex (or MS Word) homework template, which will be used throughout the quarter.

**Please read through readme.md carefully**

**After setting up the assignment environment, please look into the Jupyter notebook (*.ipynb)**

**At the end, prepare a small report on Overleaf/Word and submit the pdf to Canvas. Don't forget to PUSH your repository**

## Anaconda/Miniconda Environment Setup (Python Environment)

### Installation
This course uses **Python 3**. Python 2 will not work for these assignments, and all assignments will be graded with Python 3 on our end. Python 2 is [leaving the data science programming stack](https://pythonclock.org/) on Jan 1, 2020.

The easiest way to get set up is to use [**miniconda**](https://docs.conda.io/en/latest/miniconda.html). However, the full version of Anaconda is totally fine as well [**Anaconda**](https://docs.anaconda.com/anaconda/install/). I personally use Anaconda since it comes with a lot of functionality. Still, miniconda is the right environment for you if you have limited disk space.

Install the appropriate version of anaconda/miniconda for your operating system (select the Python 3 version). After miniconda is installed, you should be able to run `conda`. If you get an error (e.g. `-bash: conda: command not found`), make sure to source your bash file afterward (`source ~/.bash_profile` worked for Prem) or if on Windows, restart your terminal. For Windows you might need to use the "Anaconda prompt" to navigate with conda. 
It is not unheard of that people are experiencing problems installing conda on your platform. In that case, you might want to look in the system paths and replace the standard Python version with the anaconda path. Google (and stackoverflow) is also a great resource to get these problems sorted out.

### 331 Environment
Now let's create a virtual environment. Virtual environments are a simple way to isolate all the dependencies for a particular project. They make it easy to work on multiple projects without them interfering with each other (e.g., conflicting versions of libraries between tasks). 

If you are new to CONDA please read through this article. It should really help you get started and understand better what this is all about
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Now, let's get started setting everything up for 331. Here's the command:

``conda create -n NUCS331 python``

`NUCS331` is the name for the environment, and it can be used for all assignments. Its name can be whatever you want, just make sure to remember it! You can even use your *base* environment. However, we recommend using separate environments for different classes, projects, etc. 

Once the environment is created, you should activate it with:

``conda activate NUCS331``

Your shell/cmd/bash might look something like `(NUCS331) your folder/name`. The environment name is in parenthesis, indicating that it is active. If this is not the case, something likely went wrong. 

Now let's install a few packages that might come in useful throughout the course. Note that you might need to install more packages during the class. This is just a selection of packages we consider essential. You are free to install whatever package you might consider useful.

Do this by navigating to this folder's top root on the terminal and running, with your activated NUCS331 conda environment:

``pip install -r requirements.txt``

Note that we are installing many packages. This can take a while since all of those packages need to be downloaded first. If a package cannot be installed, you google to figure out what went wrong and install it manually.

Great! Your environment is all set up. You can check if those environments are correctly installed, by simply open an "ipython"-console and trying to import several of the packages in requirements.txt

## Git (Version Control)
We will use `git` for all code submissions in this class. New to `git`? Not to worry, it's quite easy! Here's a [helpful guide](https://guides.github.com/activities/hello-world/) or go through this more comprehensive [tutorial](https://git-scm.com/docs/gittutorial)

If you haven't installed GIT on your computer, please install it from [this link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

To clone this repository, install GIT on your computer and copy the link of your assignment repository. Next, you might want to create a folder called `NUCS331` to download all future assignments in this quarter. Next, `cd` into this environment where you now should find an empty folder, if nothing is downloaded yet.

Now, you have to find the link to your assignment repository above on the github page in your browser at "Clone or Download". This link might be either an SSH or HTTPS link. I recommend setting up SSH keys on your computer, which should facilitate pushing and pulling your repositories using SSH ([Link 1](https://docs.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account),[Link 2](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh))

Once you've copied the link to your keyboard, enter the following into your command-line tool (for windows, this might be the Git Bash):

``git clone INSERT-YOUR-LINK-HERE``

For HW0 this might look like:``git clone winter2022-hw0-installation-individual-jdoe95``

Once cloned, `cd` into the cloned repository. Every assignment has some files that you edit to complete it.
The problems.md gives concise instructions on what do do, so please read this first. However, the most important part is the assignment.ipynb, the Jupyter Notebook will guide you through complete homework.

## Github development cycle

All assignments are submitted via Github in this class. Once you've accepted this assignment via the Github classroom link, it made a repository of the form `https://github.com/nucs331/HW-LINK-\[your github username\]`. In the first part of this README, you cloned the repository to your local machine to develop on.

To make changes, simply open or create some file in your local version. If you created a file, you have to do:

``git add [new_file_name]`` 
you can also use
``git add .``
to add all changes in your repository; however, make sure not to include large files etc. or unnecessary files (like OS-specific files) in there. To avoid pushing these files, you can edit the .gitignore.

Git add will make `git` track the file. If you have edited an already tracked file, you don't have to add it. Then:

``git commit -m [commit_message]``

will commit the change. `commit_message` is something that describes the type of change you made. Good commit messages are descriptive, easy to understand and correspond well with the actual changes made. Finally:

```
git pull origin master
git push origin master
```

will pull the remote code and then push the commit to the repository on Github. 

**The code on the Github server (not the version on your local machine) is the code we will evaluate if you pass the assignment. If you don't push a commit, we won't see it, and we won't grade it **

## Jupyter Lab

We installed our required libraries from the requirements.txt for our environment 'NUCS331'.

Make sure that you have activated the conda environment of `NUCS331`; otherwise the packages might not be visible to you:

`conda activate NUCS331`

We will be using Jupyter Lab throughout the quarter.
Note that you can also use Jupyter Notebook and a different IDE for completing the python files.
However, we highly recommend sticking with Jupyter Lab since it provides the complete IDE experience since we have designed this course this way.

To start Jupyter Lab, the easiest way is to `cd` into the specific homework assignment (here it will be in the directory where assignment0.ipynb is present) and simply enter:

`jupyter lab`

If some problem persists after this command, the jupyter libraries might not have been installed correctly.
In that case, just run these commands and any missing components will be installed:

```
pip install ipykernel
pip install jupyter
pip install jupyterlab
```

Once you can open jupyter lab, try a simple import and see if there is no compilation issue once you execute it (using ctrl + Enter). Example:

`import numpy as np`

To use all the packages and libraries we installed in our NUCS331 conda environment, we need to create a corresponding Jupyter "environment".
(Make sure that you have activated the conda environment of `NUCS331`):

`python -m ipykernel install --name=NUCS331`

To check if this was successful:
Go to Jupyter Lab (or notebook) -> Go To "Change Kernel" option -> you should now see "NUCS331" as an option. Select that and you are good to start your assignment!

Each assignment will consist of a coding and writing task. In the initial homework, the coding and writing tasks are straightforward. They should help you get started with everything.


# Coding Task

1. Open the Jupyter Notebook (*.ipynb)
2. Implement the missing functions ( that show a `NotImplementedError` when running) in the `src` folder as indicated inside the jupyter notebook
3. Add, commit, and push your implementations to your GitHub repository. 
4. Ensure that the commits are updated on your GitHub repository **on Time before the due date**. Graders have access to your commit history and will judge according to this. The graders will check if you have an implementation in your repository, and if you fail this, this will count as a direct fail.

#  Writing Task

We have provided the option to submit a PDF report created using either LaTeX or Word. If you want to get familiar with LaTeX, this might be a good opportunity to learn but feel free to choose any format.

Please refer to the report template for the expected content and the guidelines. The questions to be answered will be at the end of the Jupyter Notebook for each homework.

## Option 1: Latex Report

Submit a PDF-file created using the Overleaf report template we provide to you. Open now the overleaf template from [here](https://www.overleaf.com/read/ybgqzfrjkzns) and [create your own copy](https://www.overleaf.com/learn/how-to/Copying_a_project#Making_a_copy_of_a_project) to start your report for homework 0.

Latex is not hard, however, if you've never used Latex before, it can be a bit overwhelming. It is a very different experience to Microsoft Word and more like writing HTML. Here are a few links that might help you get started if you are struggling with it:
1. https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes
2. http://www.docs.is.ed.ac.uk/skills/documents/3722/3722-2014.pdf

**First**, please fill out all the information on the top of the document. This means you have to include your name, e-mail address, netid, GitHub name, and the weblink to *your* assignment repository on GitHub. You'll have to do this for every homework throughout the quarter. Failing doing so will lead to immediate failure of the assignment.

In general, all scientific papers are written in a very technical style. This means there is an abstract, an introduction, methods, a result, and a conclusion section. Throughout this quarter, we are trying to adapt the technical paper writing style for all reports. 

Luckily, Latex allows you to implement and write these sections without ever worrying about your document's design since Latex is doing it all for you. To learn Latex, you will have to generate a small example PDF-report on the topic of *Computational Photography*.


## Option 2: Microsoft Word Report
Submit a PDF-file created using the MS Word report template provided. Download the template from here [template file (.docx)](./Winer_2022_NUCS 331_template.docx) and create your own copy to start your report for homework 0.

# How to submit your work

CODE: The code on the Github server (not the version on your local machine) as of the deadline is the code we evaluate your assignment on. If you don't push a commit, we won't see it, and we won't grade it.

Writing: For your writing task, **you must submit a .pdf file on Canvas.** generated through the Latex template. We will grade the last thing you put on Canvas by the deadline. You don't get credit for having the written report only in your code repository on Github. 

## Questions? Problems? Issues?

Please make sure first that something in this document doesn't already address your issue! If you still have problems, simply write on Campuswire and ask. Someone from the teaching staff will get back to you through there!

That's all! The workflow for every assignment in this class will work something like this.
