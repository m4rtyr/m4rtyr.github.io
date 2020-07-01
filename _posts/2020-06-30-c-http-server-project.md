---
layout: post
title: C HTTP Server Project
category: computer-science
tags: networking http server c pthread kqueue
use_math: false
excerpt_separator: <!--eof-->
---

I recently wanted to try out something. I wanted to create an HTTP server in the C programming language, combining `kqueue` and `pthread` to see if that creates a difference in performance compared to using either method by itself. I got this idea a few years ago when I was interested in Node.js and its method for achieving fast performance. However, the idea didn't come to fruition.

The difference between now and then is that now I like to write my thoughts down. Therefore, I've decided to write a brief outline over what I've done so far and what I plan to do in the future.

## What I've Done

So far, I've created a rough draft for a basic HTTP server in code. It's by no means perfect, but I think it serves as a good starting point. One of the things I've done is broken down the HTTP server's function into three components:

* Networking 
* HTTP 
* File System

I'll explain what each of these components do.

### Networking

The networking component deals with the transport-layer exchange between the server and the client. This is the bread-and-butter of the server since it will also be the component which will integrate the use of `pthread` and `kqueue` (though a separate component may be needed in the future). 

### HTTP

This is probably the most difficult component to implement. This component deals with the parsing and construction of HTTP messages between the server and the client. I've hesitated tackling this component because I think its a huge task in and of itself. I've thought of maybe using an external library to deal with this aspect, but I'm still debating how to approach this component.

### File System

This component deals with reading/writing to the file system. When the server needs to fetch a client a specific file, it will utilize this component. The reason this is a separate component and not directly implemented as part of the HTTP component is because I might implement caching to increase performance in the future. Additionally, if I were to extend this project further, then I might consider supporting file system operations on non-UNIX platforms as well. Melding this with the HTTP component would make the project difficult to understand, so I've considered separating this from the main HTTP component.

## Future Plans

For now, I want to create the actual HTTP server itself, simplifying the implementation as much as possible so then I can concentrate on using `kqueue` and `pthread`. I was thinking that, for the HTTP component, I would utilize another library to simplify the implementation. However, doing this might end up being more costly than just implementing the mechanism myself (plus it wouldn't really be in the spirit of things). 

In the next week, I plan to write an update to this post detailing what I've done to address these components. 

<!--eof-->