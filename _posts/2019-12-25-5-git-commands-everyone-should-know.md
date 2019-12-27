---
layout: post
title: 5 Git Commands Everyone Should Know
date: 2019-12-25 14:37:23
summary: Navigating Git is becoming more important than ever. Why not learn now?
categories: computer-science productivity
---



Git is an amazing tool for version-control and open-source collaboration (though many companies are now using it too!). I think that most people should be able to use Git, especially if it's a requirement for them at work or school. Below are 5 Git commands everyone should know.

* `git reset --hard [commit hash]` — This is fantastic as a last resort for when you've really screwed up. Generally, I've only used this when I've tried out a dumb idea (thinking it was good), merged it into my main branch, and then realized that it was, in fact, a dumb idea in the first place. [You might want to read more about this](https://git-scm.com/docs/git-reset).

* `git checkout -- [filename]` — If you're ever in a situation where you've made so many changes to a file that you think it's just better to scrap them all, this is the command. `git checkout -- [filename]` will undo any uncommitted changes to a file (or a set of files). [You might want to read more about this](https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting).

* `git rm [filename]` — This command gets git to stop tracking a file or a set of files. It's pretty useful for removing a file from the working directory and removing it from git's tracking. [You might want to read more about this](https://git-scm.com/docs/git-rm).

* `git config --global alias.[aliasname] [command]` — This is very helpful if you hate typing a lot. git alias allows you to create short-hands for common git commands. For example, `git config --global alias.nbr "checkout -b"` allows you to do `git nbr my-branch` to create a new branch called `my-branch` instead of `git checkout -b my-branch` (I made this exact alias myself). [You might want to read more about this](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases).

* `git revert` — OK, so I'll admit, I've never used this once, but I think the command is pretty useful. Given a set of commits, it'll undo those changes and record that revert in a commit. Again, I've never used it, but I can think of many cases where development can go so awry that it's necessary. [You might want to read more about this](https://git-scm.com/docs/git-revert).

Opinions? Thoughts? Praises? What are some useful git commands for you? Leave a comment below! 😀
