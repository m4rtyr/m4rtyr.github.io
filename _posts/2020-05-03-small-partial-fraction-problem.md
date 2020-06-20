---

layout: post
title: Partial Fractions and Integration
date: 2020-05-03 22:14:00
summary: A small partial fraction problem
categories: math
---

I wanted to just jot down a small problem that I solved using partial fractions. The principle behind using partial fractions is that it makes integration easier. For example, I solved the following problem today:

$$\text{Evaluate } \int \frac{x}{(x-3)(x+1)^2} dx$$

The problem is quite daunting at first but easy to solve with partial fractions. The above rational function is the sum of the following partial fractions:

$$\frac{x}{(x-3)(x+1)^2} = \frac{A}{x-3} + \frac{B}{x+1} + \frac{C}{(x+1)^2}$$

$$x = A(x+1)^2 + B(x+1)(x-3) + C(x-3)$$

From here, we can plug in $x = -1$ and $x = 3$ to solve for $A$ and $C$. From there, we can use the two results to solve for $B$ when we plug $x = 2$. That yields us $A = \frac{3}{16}, B = \frac{-3}{16}, \text{and } C = \frac{1}{4}$. 

Therefore, the integration becomes:

$$\int \frac{x}{(x-3)(x+1)^2} dx = \frac{3}{16}\int \frac{1}{x - 3} dx - \frac{3}{16}\int \frac{1}{x + 1} dx + \frac{1}{4} \int \frac{1}{(x + 1)^2} dx$$

$$= \frac{3}{16}\ln(x - 3) - \frac{3}{16}\ln(x + 1) - \frac{1}{4(x + 1)} + C$$

Simplify (5), we get $\int \frac{x}{(x-3)(x+1)^2} dx = \frac{3}{16}\ln\frac{x-3}{x+1} - \frac{1}{4(x + 1)} + C$.

I think in a future post I may explain some of the theory behind partial fractions. (2) is an especially magical statement and I think it's best to cover the topic of partial fractions in a separate article.

