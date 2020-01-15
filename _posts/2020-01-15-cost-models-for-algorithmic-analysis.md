---
layout: post
title: Cost Models for Algorithmic Analysis
date: 2020-01-15 13:23:30
summary: Cost models are a fundamental part of optimization and algorithmic analysis.
categories: computer-science
---
Recently, I [read a post](https://gregorygundersen.com/blog/2020/01/12/why-research-blog/) on HN by Gregory Gundersen on why they keep a research blog. I think the idea of having a place where you can explain things to yourself (and to others in the process) sounds quite useful. So, today I'm going to talk about cost models, an important part of algorithmic design and the theory of algorithms.

### What is a Cost Model?

A *cost model* is essentially a model to describe what operations we consider when analyzing an algorithm. For example, when stating the performance of sorting algorithms, we tend to consider *comparisons* and *array accesses* as operations that incur a cost when we execute them, so we take them into consideration when analyzing the performance of sorting algorithms. Additionally, when analyzing data-structures like LIFO stacks and FIFO queues, we tend to consider `push` and `pop` (or `enqueue` and `dequeue`) operations since these operations incur a cost. Technically, any operation (even assigning a variable) incurs a cost, but generally we're interested in operations that are complex enough that they could cause the program to slow down if executed excessively.

Knuth defined the total cost of a certain number of operations to be computed as follows:

```pseudocode
Total Cost = Frequency × Time
```

The frequency refers to the number of times the operation occurs, and the time refers to how long it takes for the operation itself to execute. For example, if a comparison took 5 seconds on average, and we did 200 comparisons, then the total cost would be 1000 seconds.

Generally, when talking about algorithmic performance, we don't talk in terms of seconds, minutes, or any unit of time, but in terms of the frequency. This is because the time it takes for an operation to be executed varies depending on the system you're running a program on. The frequency of an operation is not variable, it's well-defined. Therefore, if we know the frequency of operations, then all we need to know is the system-specific time variable to calculate the total cost (we can usually do this by just timing the operation to execute by itself).

So, when we say that an algorithm's running time is `N`^2 or `O(N^2)`, what does that mean? The latter is a bit more specific (and I may talk about it another time), but, to put it simply, an algorithm that has a running time of `N`^2 executes `N`^2 operations. What are these operations? These operations are defined by the cost model. If a sorting algorithm has a running time of `N^2` that means that, given an array of size `N`, the algorithm requires `N^2` comparisons (or array accesses, depending on what we care about) to sort the array.

### Why use a Cost Model?

I'll be honest, theoretical computer science is usually not applicable in practical situations. However, though you may not be doing any mathematical analysis, it's useful to know *what* operations are expensive and what operations aren't. Identifying what operations are the bottleneck in your application allows you to avoid premature optimization (the root of all evil) and, of course, allows you to speed up your program. Additionally, having a "mental cost model" can enable you to be more selective in your choice of algorithm or data-structure for a particular task. For example, if you're writing an IRQ handler, then a ring buffer would probably be a better than a linked-list queue since space is a premium. If you're sorting complex data types (like linked lists), then [merge sort would be a better option than quick sort.](https://stackoverflow.com/questions/5222730/why-is-merge-sort-preferred-over-quick-sort-for-sorting-linked-lists) If you're making a symbol table, you need to decide what underlying data-structure you will use according to whether your program will be performing more inserting/removing operations or accessing operations.

The idea of a cost model naturally leads to many questions pertaining to the theory of algorithms. I've listed some links below for anyone who wants to learn more.

### Resources

* [Algorithmic Analysis (Princeton)](https://algs4.cs.princeton.edu/14analysis/)
* [Asymptotic Analysis](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)
* [Grokking Algorithms](https://www.amazon.com/Grokking-Algorithms-illustrated-programmers-curious/dp/1617292230?SubscriptionId=AKIAILSHYYTFIVPWUY6Q&tag=duckduckgo-ffab-20&linkCode=xm2&camp=2025&creative=165953&creativeASIN=1617292230)
