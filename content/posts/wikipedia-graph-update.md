---
title: "Wikipedia Graph Update"
date: 2020-11-08T21:47:51-06:00
draft: false
toc: false
images:
tags:
  - computer-science
  - d3.js
---

I wanted to give a quick update on the project that I've been working on. Today, I managed to render the nodes and links on the canvas and I think I also have a better understanding of D3.js than before. Of course, I think some optimizations can be made and it can be made more graphically appealing (labels on the nodes and drag/pan/zoom are two features that I definitely want to implement soon). In particular, I think nodes that are not within the a certain range of the current client's view should not be drawn onto the Canvas until the client drags the Canvas to that area (for example, if something is a few 100 pixels outside of the border, then we don't draw it onto the Canvas until the client is near that region).

That's all for now; I hope to give more updates tomorrow.