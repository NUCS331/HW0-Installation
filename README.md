# HW0: Environment setup for EECS 331 @ NU

In this initial assignment, the goals are:

1. to set up a working programming environment using either conda or virtualenv environments.
2. to get acclimated to the "pull, commit, push" development cycle for git. All programming assignments in this course will be submitted via Github (all free-response quesitons will be submitted via Canvas).
3. to get acclimated with Jupyter Lab which is required for all assignments in this course.

**Please read through readme.md carefully**

**After setting up the assignment environment, please look into the problems.md and after into the Jupyter notebook**

**At the end, prepare a small report on Overleaf and submit the pdf to Canvas. Don't forget to PUSH your repository**

## Anaconda/Miniconda Environment Setup (Python Environment)

### Installation
This course uses **Python 3**. Python 2 will not work for these assignments and all assignments will be graded with Python 3 on our end. Python 2 is [leaving the data science programming stack](https://pythonclock.org/) on Jan 1 2020.

The easiest way to get setup is to use [**miniconda**](https://docs.conda.io/en/latest/miniconda.html). However, the full version of Anaconda is totally fine as well [**Anaconda**](https://docs.anaconda.com/anaconda/install/). I personally use Anaconda since it comes with a lot functionality, but if you have limited disk space miniconda is the right environment for you.

Install the appropriate version of anaconda/miniconda for your operating system (take care to select the Python 3 version). After miniconda is installed, you should be able to run `conda`. If you get an error (e.g. `-bash: conda: command not found`), make sure to source your bash file afterwards (`source ~/.bash_profile` worked for Prem) or if on Windows, restart your terminal. For Windows you might need to use the "Anaconda prompt" to navigate with conda. If you're experiencing problems installing conda on your platform you might want to look in the system paths and replace the standard Python version with the anaconda path.

### 331 Environment
Now let's create a virtual environment. Virtual environments are a simple way to isolate all the dependencies for a particular project, making it easy to work on multiple projects at once without them interfering with each other (e.g. conflicting versions of libraries between projects). 

If you are new to CONDA please read through this article. It should really help you getting started and understand better what this is all about
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Now, let's get started setting everything up for 331. Here's the command:

``conda create -n NUCS331 python``

`NUCS331` is the name for the environment and it can be used for all assignments. The name can be whatever you want, just make sure to remember it! You can even use your *base* environment, however we recommend using seperate environments for different classes, projects etc. 

Once the environment is created you should activate it with:

``conda activate NUCS331``

Your shell/cmd/bash might look something like `(NUCS331) your folder/name`. The environment name is in parenthesis, indicating that it is active, if this is not the case something likely went wrong. 

Now let's install a few packages that might come in useful throughout the course. Note that you might need to install more packages during the class and this is just a selection of packages we consider important. You are free to install whatever package you might consider useful.

Do this by navigating to the top root of this folder on the terminal and running, with your activated NUCS331 conda environment:

``pip install -r requirements.txt``

Note that we are installing many packages. This can take a while since all of those packages need to be downloaded first.

Great! Your environment is all set up. You can check if those environments are correctly installed, by simply open an "ipython"-console and trying to import several of the packages in requirements.txt

## Git (Version Control)
We will use `git` for all code submissions in this class. New to `git`? Not to worry, it's quite easy! Here's a [helpful guide](https://guides.github.com/activities/hello-world/) or go through this more comprehensive [tutorial](https://git-scm.com/docs/gittutorial)

If you haven't installed GIT on your computer please install it from [this link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

To clone this repository install GIT on your computer and copy the link of your assignment repository. Next, you might want to create a folder called `NUCS331` where you will download all future assignments in this quarter. Next, `cd` into this environment where you now should find an empty folder, if nothing is downloaded yet.

Now, you have to find the link to your assignment repository above on the github page in your browser at "Clone or Download". This link might be either a SSH or HTTPS link. I recommend setting up SSH keys on your computer which should facilitate pushing and pulling your repositories using SSH ([Link 1](https://docs.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account),[Link 2](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh))

Once you've copied the link to your keyboard, enter the following into your command line tool (for windows this might be the Git Bash):

``git clone INSERT-YOUR-LINK-HERE``

For HW0 this might look like:``git clone fall20200-hw0-installation-jdoe95``

Once cloned, `cd` into the cloned repository. Every assignment has some files that you edit to complete it.
The problems.md gives very short instructions on what do do, so please read this first. However the most important part is the assignment.ipynb which is the Jupyter Notebook which will guide you through the complete homework.

We will play around with GIT a little bit more throughout the installation assignment. The exact instructions on what to do and what to report are written in the problems.md and when you open the jupyter notebook.

## Jupyter Lab

We will be using Jupyter Lab throughout the quarter. Note, that you can also use Jupyter Notebook and a different IDE for completing the python files. However, we highly recommend sticking with Jupyter Lab since it provides the complete IDE experience and it is the way we have designed this course.

In order to start Jupyter Lab, the easiest way is to `cd` into the specific homework assignment and simply enter:
`jupyter lab`

Make sure thast you have activated the conda environment of `NUCS331`, otherwise the packages might not be visible to you.
