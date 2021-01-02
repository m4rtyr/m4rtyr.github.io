---
title: "Trying Server Side Charts"
date: 2020-11-05T20:36:18-06:00
draft: false
toc: false
images:
tags:
  - untagged
---

Hey there.

This is sort of an update to the article I wrote on trying to use D3.js network charts with canvas. However, after being away from this project for over two weeks and trying out Canvases, I realized a few things:

1. Generating graphs with millions of nodes on the client side is *horrible*. If it were just a few thousand nodes, then it would be ok, but I'm generating so many nodes that many clients wouldn't be able to handle it on their machine (regardless of whether we use Canvas or SVG).
2. I'm not sure how interactive my graph will be, so I'm assuming for now that it'll be completely static.
3. Generating graphs on the server-side as an image is more effective than sending a huge list of nodes and links to the client.

In the following weeks, I hope to try generating graphs on the server side and then serving it to the client.