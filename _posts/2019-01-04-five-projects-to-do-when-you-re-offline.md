---
layout: post
title: 5 Projects To Do When You're Offline
date: 2020-01-04 22:54:01
summary: When you're bored, out in the wilderness, or just want to do something productive.
categories: computer-science productivity
---

Recently, I went on a camping trip with family and I got **really** bored. The outdoors isn't really my thing (which is why I decided that programming and mathematics suit me more than, say, being a gym instructor), so I naturally brought my computer and phone along with me. Of course, I had no service and no Wi-Fi meaning that I was limited in terms of what I could do. The only real form of entertainment I had was my downloaded music and my text editor.

A lot of code written nowadays requires some sort of Internet connection. Building a web server? Internet. Developing a vast neural network? Internet. Making an app? Internet. Creating a website? Internet.

Many of the tools that typical developers make require an Internet connection. Additionally, I assume there are some developers that — like me — would prefer to spend a weekend inside rather than let the sun touch their face or would just like to spend some time doing something productive.

If you're that type of person, then this article (might) interest you if you (might) find yourself in this situation. If being Internet-isolated is not a problem for you, then please don't recommend that I go outside more because — and this might be a shocker — *I don't care*. At all.

Without further ado, the following are [5 projects to when you're do offline](https://github.com/m4rtyr/5-projects-to-do-offline).

### A Basic Calculator

I was looking at my phone thinking about what I could do. The calculator app is one of the only functional apps on your phone. I thought I would make a basic calculator on the terminal (like `bc`) that could perform addition, subtraction, multiplication, division, and exponentiation according to the order of operations. Additionally, I wanted it to be able to evaluate parenthesized expressions. After a little bit of thinking, [I created a basic calculator](https://github.com/m4rtyr/5-projects-to-do-offline/tree/master/calculator) in C.

### A File Search Program

Since I can't access any data on the cloud, I only have the files on my local machine to deal with. So, logically, making a file search program makes sense. I wanted it to be simple, so I decided to ignore character files, symbolic links, and block devices. With a majority of the file system minutiae out of the way, we only have to consider directories and regular files. If we come across a directory, then we put all the contents of the directory into a queue. Otherwise, if we come across a regular file, we check to see that the regular file's name matches the user's search query. In a little bit of code, [I made a crude file search program](https://github.com/m4rtyr/5-projects-to-do-offline/tree/master/file_search) (again, in C).

### Any UNIX Tool

There are a lot of UNIX tools: `less`, `grep`, `du`, `cat`, `rm`, `ld`, and `ps`, to name only a few. If you're on a UNIX system, then pick a UNIX tool to recreate. Generally, most of the knowledge needed to recreate these tools can be found within a few man pages or with just a bit of basic programming knowledge. If you're on Windows, then this task can be especially challenging. [I chose to make a basic version of `grep`](https://github.com/m4rtyr/5-projects-to-do-offline/tree/master/grep) (with highlighting).

### Play with Mazes

Generating random mazes is surprisingly fun and a real algorithmic challenge. The only reason I'm even suggesting this is because of Jamis Buck's *Mazes for Programmers*, a thrilling book (that I should have taken with me when I was camping) on maze algorithms. The book is entirely in Ruby, but it can be done in any language. I wrote some basic code to [generate a maze](https://github.com/m4rtyr/5-projects-to-do-offline/tree/master/mazes) of arbitrary size according to user input and output it to the terminal screen using the Binary Tree algorithm (**Disclaimer**: OK, so I didn't write this code, the author of the book did, but that's besides the point). If you're ever feeling uncreative (like I was when thinking of a project to do), then I would recommend just going through this book. So far, it's been quite entertaining.

### Recreate Basic Programming Language Features

Another project is to recreate basic features of your programming language of choice in that programming language. I didn't "recreate" `malloc()` and `calloc()` *per se*, but I did implement a simple, dumb [variant of the two functions](https://github.com/m4rtyr/5-projects-to-do-offline/tree/master/alloc) that allocates memory off of a fixed memory pool. Of course, there's many other features you can recreate: slices, vectors, lists, dictionaries, even `for` and `while` loops. The choice just depends on what seems interesting to you.

### Conclusion

Again, all the projects I did above are available in [this repository](https://github.com/m4rtyr/5-projects-to-do-offline). Some of them can obviously be improved. For example, the calculator could have its own GUI (maybe not in C, but in another language) or handle more complex functions like `sin` and square root. The file search program is single-threaded and synchronous. Could an async/threaded approach be faster? The `alloc` program is a really dumb implementation of a memory allocation system. There's not even a way to free up memory. Maybe a binary heap would be better (or a Fibonacci heap) rather than a linear, fixed memory pool? The list of improvements are endless.

Of course, there's many, many more offline projects you can do. Pong, Chess, a JSON parsing library, or even an entirely new programming language are all examples of offline projects that you can embark on.

Have you done any interesting projects while offline? Have any thoughts? Opinions? Concerns? Ideas? Write a comment below! 😁
