---
title: "Combining Canvas and D3.js Network Charts"
date: 2020-11-03T18:10:06-06:00
draft: false
toc: false
images:
tags:
  - d3.js
  - computer-science
  - javascript
---

I've been working on creating a network graph to show the relationship between every single Wikipedia article. I wanted to write this article so I can walk through the problem I'm having.

## The Problem

Basically, when I tried to render the network chart I decided to go the conventional route and use an SVG (Scalable Vector Graphic). SVGs are awesome for rendering different types of shapes and transitions. For a typical person rendering a few nodes on a network graph, SVGs work well (not to mention that pretty much every tutorial/article on using D3.js to build network graphs uses SVGs).

The problem is that I want to render millions of nodes with potentially millions of links and SVGs tend to perform terribly when only a few thousand nodes are rendered.

## The Solution

One solution that I've found that I want to try is using the Canvas API to render the network chart while exploiting D3.js's data binding and force simulation capabilities to create the graph. From what I've researched, the Canvas API is pretty lightweight and it (possibly) can handle drawing millions of nodes and links to the screen. With that in mind, I want to roughly outline what I'm planning to do:

*  Create a custom DOM element called `dummy`.
* Under `dummy`, create classes `dummy.link` and `dummy.node` and set the appropriate attributes for these classes.
* Run `forceSimulation()` to calculate position of nodes every time new data is added.
* After the force simulation has run, draw the nodes on the canvas using the attributes set on `dummy.link` and `dummy.node` (which includes not only their positions but also their color, thickness, radius/length, etc).
