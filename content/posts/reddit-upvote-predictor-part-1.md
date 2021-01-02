---
title: "Reddit Upvote Predictor Part 1"
date: 2020-12-02T22:44:50-06:00
draft: false
toc: false
images:
tags:
  - machine-learning
  - computer-science
  - python
  - matplotlib
---

Hey there.

I wanted to start working more with Tensorflow, so I decided to do a simple project where I try to predict the number of upvotes a given Reddit post will receive in a certain amount of time.

This project is very suitable for machine learning, since the number of upvotes $y$ that a post gets can be predicted using a linear equation, of the form $\sum_{i=1}^n w_ix_i+b_i$ where $w_i$ and $b_i$ can be calculated through a method such as gradient descent and $x_i$ is the feature in particular.

I decided, initially, to consider 4 features when determining the number of upvotes a given post will receive:

* OP's Karma
* Time since posted
* Comments on post
* Subreddit the post was posted in

Intuitively, these features would seem to have some predictive power. However, before I could start implementing a model like this, I decided that I wanted to graph the data. I used the PRAW API in Python to obtain the top 1000 posts in each of the most popular subreddits (as determined by `pr.subreddits.popular()` where `pr` is an instance of `praw.Reddit`). I tried to make it a little faster by using `concurrent.futures` to send the requests concurrently. Despite my efforts, it still took a little while, but after I got the data, I plotted the data with matplotlib:

![4 subplots with karma, time since posted, post comments count, and subreddit graphed against upvotes](/upvotes-graph.png)

Clearly, the upvotes on a post appear to be heavily influenced by the time since it was posted (the x-axis is in seconds since the Epoch — January 1st, 1970 00:00) and also by the subreddit it was posted in, with r/memes garnering a heavy number of upvotes (the number of upvotes for each bar is cumulative, i.e, in a given subreddit, all the upvotes received by the 1000 posts examined were added together). It also seems that there is a moderate relationship between the number of comments and the number of upvotes and, surprisingly, a *negative* relationship between the number of upvotes and karma of the OP. 

After viewing the graph, I'm thinking maybe gradient descent with nonlinear feature transformations would be applicable in this scenario and it seems that [mathematically it's an extension of the same principles](https://jermwatt.github.io/machine_learning_refined/notes/10_Nonlinear_intro/10_2_Regression.html) used in linear regression. Regardless, gradient descent definitely seems applicable here, and it seems that the features chosen can be used to predict, to a certain extent, the number of upvotes a post will receive.

