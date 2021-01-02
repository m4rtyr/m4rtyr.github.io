---
title: "Why I Stopped Using Lastpass"
date: 2020-11-04T21:48:11-06:00
draft: false
toc: false
images:
tags:
  - personal
---

For the longest time I used to use Lastpass. It's a pretty good password manager, but over time I started to have some concerns about whether I should keep using it. So, a few months ago, I deleted my Lastpass account and decided to get a local password manager. 

So, why did I do it?

Lastpass is a great password manager without a doubt. Not only is it free, but you can auto-generate secure, random passwords and with its browser extension you can auto-fill password and username fields to make logging into your accounts faster. It's great. However, I started to feel insecure about using Lastpass when I realized that using a *browser extension* to store my passwords is a little insecure. If a website exploited a weakness in my browser, they could potentially gain access to my passwords if I were logged into my Lastpass account. Granted, I thought, this isn't likely to happen since I tend to follow good security practices which means (1) not going to sketchy websites and (2) enabling my firewall when I connect to any network. 

However, a more likely attack vector is at the company itself. You see, Lastpass doesn't store your passwords locally. Instead, all of your account passwords are stored in some database that Lastpass owns in some part of the world unknown to you. Considering that data breaches happen frequently and a company like Lastpass is a desirable target for any bad actor, it's possible that my data could be leaked in a data breach of Lastpass's servers. I know that Lastpass has a good reputation and that they probably follow good security practices, but I feel a little insecure entrusting the integrity of my accounts to a company.

As a result, I deleted my Lastpass account and found a secure local password manager that would suit my needs. Sure, it may not be as convenient as using the Lastpass browser extension, but I feel better knowing that my passwords are stored, encrypted and hashed, in a local database on my computer rather than in some database waiting to be leaked by a hacker.

NOTE: When choosing a local password manager, I ignored managers like 1Password and BitWarden because (1) they're paid and (2) they also have some of the same faults that Lastpass has. 