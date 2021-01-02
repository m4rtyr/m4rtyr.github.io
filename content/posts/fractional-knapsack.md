---
title: "Fractional Knapsack"
date: 2020-11-06T20:17:22-06:00
draft: false
toc: false
images:
tags:
  - computer-science
  - algorithm
  - dynamic-programming
---

I wanted to explain the fractional knapsack algorithm since I recently solved a programming problem with it. However, I don't want to try and explain the algorithm by just listing out the steps. Instead, I want to provide an intuitive description of the algorithm whereby I explain each step as we try to solve the problem.

## Problem

Given $n$ items each of which have a weight $w_k$ and price $p_k$, choose the items (not necessarily all) such that you choose the minimal price and the weight of the items is $\le W$.

## Solution

In this case, we want to do the following:

$$\text{minimize} \sum_{k=1}^n p_kx_k$$

where $x_k$ is the fraction of the item we took. We do this with the constraint that:

$$\sum_{k=1}^n x_kw_k = W$$

where $0 \le x_k \le 1$ is the fraction of the item we take. 

Considering that each item is of weight $w_k$ and has price $p_k$, a greedy solution would be to choose the object with minimal price first. In order to choose the object of minimal weight, we can sort the objects by price per unit weight in ascending order. That way, we choose the object of minimum price each time. Thus, we sort according to $\frac{p_k}{w_k}$. Let's use an example. Imagine we have some items with the following weights and price and we can only carry 500 pounds:

* 100 pounds, $30 (unit rate: \\$0.3)
* 20 pounds, $5 (unit rate: \\$0.25)
* 150 pounds, $25 (unit rate: \\$0.17)
* 225 pounds, $15 (unit rate: \\$0.07)
* 10 pounds, $2 (unit rate: \\$0.20)

Sorting the above list in ascending order, we get:

* 225 pounds, $15
* 150 pounds, $25
* 10 pounds, $2
* 20 pounds, $5
* 100 pounds, $30

Now, considering that we must "fill the knapsack" with a weight of $W$, we should continue to take as much weight as possible until we are forced to take a fraction to prevent overfilling the knapsack. So, in the example above, we would take the 225 pounds for \\$15 (225 < 500), the 150 pounds for \\$25 (225 + 150 = 375 < 500), the 10 pounds for \\$2 (225 + 150 + 10 = 385 < 500), and the 20 pounds for \\$5 (225 + 150 + 10 + 20 = 405 < 500). However, once we arrive at the 100 pound item, we are forced to take a fraction since if we take the whole 100 pounds the knapsack would fill to 505 pounds which is above the knapsack capacity. Thus, we take 95 pounds (as a fraction, that is $\frac{95}{100}$ of the item) which would mean that we would only pay $\\$0.3 \times 95 = \\$28.50$. Thus, in total, we would pay $\\$15 + \\$25 + \\$2 + \\$5 + \\$28.50 = \\$75.50$. Thus, with the fractional knapsack algorithm, we would have found the lowest price.

The above algorithm would run in $O(N \log N)$ if we consider that we sort the items by their price per unit and then check what fraction of the item must be added.  



