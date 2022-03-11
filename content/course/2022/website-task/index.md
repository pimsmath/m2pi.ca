---
title: "Team Website Building"
authors: [iana]

summary: |
  Participants will use python and jupyter to explore real world datasets and
  extract insights from them.


tags: ['2021']
categories: []
date: 2021-07-25T16:58:18-07:00

external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---
### Description

The purpose of this "course" is to add/update your profiles on the m2pi.ca
website so that people can find the great work you're about to do! Well split
the session into two parts: In the first part we will use a common GitHub
workflow (Pull Requests) to add profiles to the m2pi.ca website. In the second
part (optional attendance) we will look at the system used to build the website
and how you can use the same continuous integration tools to build a website for
yourself or your team.


### Part 1

The m2pi.ca website is a static site build from [this
repository](https://github.com/pimsmath/m2pi.ca). We would like to include
profiles for each of you on this website to help showcase your work. Since the
website content is stored on GitHub we will take this opportunity to demonstrate
a common but relatively advanced GitHub workflow to let you make the changes
yourself.

#### Pull Requests: The basic idea

In your git and GitHub class you learned about using git as a tool for version
control and how to set up remote repositories on GitHub. The main reason for
hosting repositories in a public place like GitHub is so that you can share them
and collaborate with others (e.g. Include a new feature you hadn't thought of).

One model for managing a collaborative workflow is to give people write
permission on your repository. This can work with people you trust, but it can
be risky for others and can have unintended consequences; what if you only
wanted someone was added to help you with the documentation but decided to
reimplement everything in Fortran.

The most common alternative is the
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) + [Pull Request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) workflow. This is a very popular pattern which lets people _propose_ changes and then discuss them with the project maintainers until everyone is happy.

If you remember Marie's discussion of git, when you clone a repository, a
clone is a *complete* working copy including the entire project history
(commits) from the original. When you Fork a repository on github a clone of the
original is added to _your account_. You are free to make any edits you like to
your fork (you have write permission on it) but crucially it will share a common
history with the original. This means your changes can be isolated, reviewed and
ultimately merged. In practice the workflow typically goes like this

  1. Make a fork of `m2pi/super-project` as `myusername/super-project`
  2. Make a new branch on your fork. Most new work happens in branches so
     that you can keep things tidy
  3. Open a pull request for your new branch against the main branch of
     `m2pi/super-project`
  4. The m2pi admins look at your changes. They'll discuss your changes via
     comments on the pull request. They might request you make changes and push
     new commits to your branch.
  5. When everyone is happy the m2pi admins will merge your pull request which
     will update the original `m2pi/super-project` repository. Job Done!

This workflow lets any random person propose changes against any public
repository and forms the foundation of a lot of software development workflows.
Of course there are lots of variations (maybe you have merge conflicts, or the
admins want you to rebase before committing etc.) but this is the general
pattern.

#### Pull Requests: In Practice

Please follow the steps below to complete this part of the training:

1. Visit the [m2pi.ca github repository](https://github.com/pimsmath/m2pi.ca). In
the top right hand corner, hit the `fork` button.
1. If you are asked "Where should we fork m2pi.ca" select _your_ GitHub account

GitHub will say it is forking m2pi.ca for you. When it is finished it will take
you to *your fork* of the m2pi.ca website. If you look at the repository name in
the top right it will say something like "`yourusername/m2pi.ca` forked from
`pimsmath/m2pi.ca`".

> There are a few ways to complete the steps below. I'll do it directly through
> GitHub but if you have already set up your ssh keys for GitHub you can do this
> quickly on the CLI.

We should create a new feature branch before making any changes.

1. At the top left of the repository, click on the branch button, it will
   currently say `master`.
1. In the little dialog that opens add a new branch name. Something like
   `yourusername-new-profile` will work (replacing `yourusername`). Avoid spaces
   or other special characters in the branch name.
1. Below the text area click `create branch:
   yourusername-new-profile`
1. This will create a new branch in your fork of the repo on GitHub. The branch
   button should now display your branch name.

We are ready to add the new profile information.

1. Click on `content -> authors`. Each of the folders/directories shown
   corresponds to a user profile on the website. **Make sure you are in the
   right directory before proceeding**.
1. Click `Add file -> Create new file`. This will open up a basic text editor on
   GitHub asking for a filename. We need to create a folder with your github
   username and a file called `_index.html` (the underscore is important!)
   inside that folder. It isn't obvious how to create a folder, but if you type
   your GitHub username in the filename box then type a forward slash (`/`)
   GitHub should understand what you mean. Add `_index.md` as the filename.
1. In the body of the file paste the following text
```
---
# Display name
title: Your Name Goes Here

# Username (this should match your github username)
authors:
- YourGitHubUsername

# Role/position e.g. Graduate student
role: Postdoctoral Fellow

# Organization membership
Organizations/Affiliations:
organizations:
- name: Your Current University
  url: https://www.google.ca

# A list of your interests, add as many as you want
interests:
- Scientific Machine Learning
- General Purpose Data Science
- Mathematical Biology

# Your educational history, add as many as you want
education:
  courses:
  - course: PhD - Applied Mathematics
    institution: Univerisity of Alberta
  - course: BSc - Mathematics
    institution: Universidad of British Columbia

# Social/Academic Networking, delete any items you don't want to use
social:
- icon: github
  icon_pack: fab
  link: https://github.com/pimsmath
- icon: twitter
  icon_pack: fab
  link: https://twitter.com/carlosshigoto
#- icon: linkedin
#  icon_pack: fab
#  link: https://www.linkedin.com/in/carloscontrerasc/

user_groups:
- committee: members
  role: Project 1 member

tags:
- '2021'
---
This is a freeform text area which supports markdown syntax. Fill in a couple of
sentences describing yourself.
```
Some notes about the syntax of the file:
1. There are two parts of the file: Metadata and Markdown. The Metadata makes up
   most of the file and is enclosed between lines containing three dashes
   (`---`). Fields inside the metadata area use YAML syntax.
1. Most of the YAML fields are specified as `key: value` pairs. Look at each
   field and updated if necessary. Make sure to update at least your name,
   github username and affiliation.
1. Be very careful with syntax. YAML is sensitive to errors. whitespace and case
   matter!
1. At the bottom of the file (after the last `---`) you enter the markdown
   area. You can add a free-form paragraph in markdown format to describe
   yourself.

At the bottom of the webpage you will see a space for a commit message and some
options. Add a short commit message in the first box e.g. "Adding profile for
YOUR NAME". There is also a radio button which will tell you where your commit
is going. Make sure it says the name of your new branch (e.g.
`yourusername-new-profile`). Hit the green `Create new Commit` button. 

You should be looking at the GitHub File brower again and the breadcrumb at the
top of the page should say something like
`m2pi.ca/content/authors/YourGitHubUsername`. Assuming it does, the last task is
to add a profile picture of yourself. Please try to find a photo of yourself
somewhere and save the file as `avatar.jpg` somewhere on your computer. 

1. Select `Add file -> Upload File`.
1. In the dialog that opens up, click `Choose your files`, then browse your
   computer to find wherever you saved `avatar.jpg` and select it.
1. Add a commit message (e.g. "Adding photo"), make sure you are commiting to
   your feature branch and hit `Commit Changes`.

If all has gone well, GitHub will have noticed that you have a new feature
branch and offer to help you make a pull request. Click the Green `Compare and
Pull Request` button. In the new window which opens you will be sending a
message to the m2pi admins. Add a message describing your changes and hit the
green `Create Pull Request` button.

In a typical workflow you would now be expected to keep an eye on that pull
request for any discussion with the project maintainers. This can sometimes be a
long process but since our changes are pretty simple that shouldn't be too
complicated. You might notice some automatic messages attached to your pull
request related to building a preview of the website. If the preview looks good
with your changes I'll try to merge it right away. If there are any problems
I'll send you some instructions via the comment area in your pull request.



## Part 2

m2pi.ca is a static website. This means that it consists of static components
like html, javascript and css files. These files are hosted somewhere for us and
when you visit the site they are sent to your browser to interpret.  There is no
stateful backend (database) powering the website, so the site can be relatively
light weight and easy to maintain. Static websites have exploded in popularity
in recent years and in this part of the session we'll explain how you can use a
static website builder with GitHub and a service called Netlify to build and
host simple websites (e.g. resume sites or project sites).

1. Install [hugo](https://gohugo.io/)
1. `hugo new site teamX-project-site`
1. `git init` the new site
1. `git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git
   themes/ananke`
1. Add `ananke` to `config.toml`
1. `hugo serve -D` to preview your site at http://127.0.0.1:1313
1. hugo new post/kickoff.md
1. Change background image and color
1. Push repo to github
1. Connect repo to netlify
1. Specify netlify config in `netlify.toml`
1. Create a branch and add mathjax
1. Preview deploy branch
1. Merge PR to publish to live site.
