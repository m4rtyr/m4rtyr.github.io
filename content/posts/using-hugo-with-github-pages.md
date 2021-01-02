---
title: "Using Hugo With Github Pages"
date: 2020-09-05T20:41:21-05:00
draft: false
toc: false
images:
tags:
  - github-pages
  - hugo
  - blogging
---

Hey there!

I just moved my blog from Jekyll to Hugo and I wanted to give a quick tutorial on how to use Hugo with GitHub pages. 

## Installation

First, you'll need to install Hugo:

MacOS: `brew install hugo`

Linux: `brew install hugo` (Here's a link on [how to install `brew` for Linux](https://docs.brew.sh/Homebrew-on-Linux))

Windows: `choco install hugo -confirm` or `scoop install hugo`

*Note: You may need to install Go.*

## Hugo on GitHub Pages

Installing Hugo for GitHub Pages is pretty simple. First, we will create a new directory (I'll refer to this directory as `mysite`). Then, type the following commands:

```shell
> hugo new site mysite
> cd mysite
```

If you type `ls`, you'll see a bunch of files in this directory. The only one we care about for now is `config.toml`. Go to `config.toml` and find the line that says `publishDir = public` (or add it somewhere if it's not present). Set `publishDir` to `docs`. This will be the root directory that GitHub pages will use to deploy our site. Also, find the line with the parameter `baseURL` and set `baseURL = https://<YOUR-USERNAME>.github.io` where `<YOUR-USERNAME>` is your GitHub username.  

Now, type the following:

```shell
> hugo server -D
```

Go to [https://localhost:1313/](https://localhost:1313) and confirm that your site is running properly. Then, go to GitHub and make a new repository called `<YOUR-USERNAME>.github.io`. Once you do that, go to the **Settings** tab and scroll down to the section that says **GitHub Pages**. Under the **Source** heading, use the dropdown to select the `/docs` option. This will inform GitHub Pages that the root directory for your site is under the `docs` subdirectory. Finally, click the **Save** button.

![test](/github-pages.png)

All we have to do now is push your site to the repository. Type the following commands (you're still in the `mysite/` folder at this point):

```shell
> cd ../
> git clone https://<YOUR-USERNAME>.github.io
> cp -r mysite/ <YOUR-USERNAME>.github.io
> rm -rf mysite/
> cd <YOUR-USERNAME>.github.io
> hugo
> cd docs
> git add .
> git commit -m "My Hugo Site" # or whatever you want your commit message to be...
> git push origin master
```

...and that's it! The above commands clone your repository, copy the files from `mysite/` to `<YOUR-USERNAME>.github.io/`, generate the root directory (`docs`) using the `Hugo` command, and then commit and push your site to the `master` branch.

Likely, you'll be making a lot of changes to your Hugo site. In that case, you'll want a shell script to streamline the process. The following bash script does that:

```shell
#!/bin/sh

# If a command fails then the deploy stops
set -e

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

# Build the project.
hugo # if using a theme, replace with `hugo -t <YOURTHEME>`

# Go To docs folder
cd docs

# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master
```

The above was taken from a post by Hugo for deploying your website to GitHub pages, which I [recommend reading](https://gohugo.io/hosting-and-deployment/hosting-on-github/) for more information on how to add posts, customize/create themes, and write your own templates.

