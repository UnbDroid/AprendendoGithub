# Git Course

## Introduction

The repository is only to learning git. By that way, all the files in this repository are examples.

We have GitHub, it's a plataform about git. It doesn't matter understanding what is that if we have only to use. So, our objective is how to use git. By that way, always we say "learning git" that means the same of "learning how to use the git".

The frist thing we have to know is some basics about git. All we need to know is that Git is like a Cloud. You can put in it your archives, texts, codes and whatever you want. Is there a limit to use git, like storage space? I don't know, but if you only put small and necessary archives, it will be almost unlimited.

We will use the GitHub plataform. Where you can acess throught the link ```https://github.com/``` and doesn't need to pay to use it. You can pay for some advantages, but it's useless for our objective.

Why will we use it? Because it's free, usefull for share codes, simple and it has a powerfull version control system that we will learn further.

## Objective

Learning Git, we will use it for share codes and controling versions of the codes

## Installing and configuring the necessary

To all the course, we are going to install 3 softwares:

* The git
* A text editor
* A diff tool

Their uses are shown below.

### Installing the git

Frist of all, we have to install te git on your machine. If you are using some Linux distribution, for example Ubuntu, you only have to type on your terminal:

```sudo apt-get install git```

### Installing a text editor

For editing our files, it is necessary a good text editor and the tools which are very usefull. Because most of the people of Droid-UnB know the Sublime. By that way, we are going to show how to install the sublime. If you are using another text editor like ```Notepad++```, ```TextMate 2```, ```Kate``` or ```Gedit```, maybe they are very good and usefull, however it is not guaranteed that texteditors works well with git.

[The sublime website](https://www.sublimetext.com/)

If you are using Ubuntu or Debian, you have just to type these 5 commands:

```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text
```

If you are using another Linux's distribution, see the link below.

These commands were gotten through this [link](https://www.sublimetext.com/docs/3/linux_repositories.html) on 27th jan 2018. If it's not working, follow the website instructions

### Visual Merge and Diff tool installation

For futher use, we have to install a difftool. The Difftool which we are going to use is the [P4Merge](https://www.perforce.com/products/helix-core-apps/merge-diff-tool-p4merge).

To install the tool on Ubuntu, we are going to use the tutorial: [How to install P4merge on Ubuntu](http://blogs.pdmlab.com/alexander.zeitler/articles/installing-and-configuring-p4merge-for-git-on-ubuntu/)

Frist of all, download the file selecting your computer configurations through the link: [Visual merge tool - Downloads](https://www.perforce.com/downloads/visual-merge-tool).

## The basic



### Starting creating a new repository



### Joining in some existing repository



### Add, commit, push, pull and the basic workflow.

We have few basic commands but they are all import 

There a representation that we call ```Basic Git Workflow``` and inside it we have 4 stages that we call:

* Working Directory
* Staging Area
* Repository
* Remote

Only the last is ```Remote```, the rest are ```Local```. That means that only the fourth depend upon the internet and who acess the ```github.com``` will see the last one.

## History and versions



## Branching and Merging



## Rebasing



## Stashing



## Tagging



## Usefull links

We have some usefull links that help us with a lot of things. Below are showen they funcionality.

* [Sublime](https://www.sublimetext.com/) - The sublimetext's website
* [P4Merge](https://www.perforce.com/products/helix-core-apps/merge-diff-tool-p4merge) - A good tool for merging
* [Hipsum](https://hipsum.co/) - A website that give us some text.
* [Meettheipsums](http://meettheipsums.com/) - If you understood the link below, there are a lot of websites with the same purpuse. Meet them through this link
* [A good README template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) - This link show some readme simple examples 
* [Mastering markdown](https://guides.github.com/features/mastering-markdown/) - If you wanna know more about markdown

## Credits

Name | Email
---- | -----
Carlos Adir | carlos.adir.leite@gmail.com
