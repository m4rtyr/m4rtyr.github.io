---

layout: post
title: "C Algorithms and Data Structures Library: Part I"
date: 2020-05-16 21:16:00
summary: Refers to the library I'm creating for animating common algorithms and data-structures.
categories: computer-science programming project
---

*I haven't been very consistent with posting everyday because I have exams. Hopefully I'll be able to write more after my exams are over*.

In this post I wanted to discuss about a project that I am working on. The project is to create a library for algorithms and data structures in C with the ability to animate these algorithms and data structures so that the user can gain more insight into their properties and, most imporantly, their internal functionality. Ideally, I would also like to document certain properties about these algorithms and data structures, including their time complexity, space complexity, and correctness.

Obviously, this project is the type that will never be complete. There are a plethora of algorithms and data structures and new computational methods and information structures will continue to be produced. Therefore, the repository is not meant to be complete. Rather, it is meant to document the most common algorithms and data structures while providing visual animations that can help the user understand them. For example, in the future, a LIFO stack will be added as one of the data structures in this library. However, along with the code for this data structure, a separate animation module (which can be toggled on/off by the user) will allow the user to watch the stack in action as items are pushed on and popped off it.

Over the past few days, I've been mainly working on creating some of the boilerplate and common structures and routines (henceforth referred to as CSR) for this library. Naturally, it's hard to know what CSR are necessary since every algorithm and data structure is unique. As of right now, the only CSR that will clearly be useful for implementing future algorithms and data structures is a generic type which is currently defined in the library as a structure called `GENERIC`. However, instead of predicting what is necessary for implementing the expansive list of algorithms and data structures ahead of time, I decided to divide the library into sections and subsections, working on specific subsections and adding boilerplate and CSR as needed. Therefore, I can implement the algorithms and data structures without worrying about the library as a whole. The following is my directory structure:

```
- algorithms/
  - animate/
  - combinatorial/
  - numerical/
  - searching/
  - sorting/
  - types.h
- data-structures/
```



The above shows a superficial diagram of my directory structure (the full repository is [here](https://github.com/simulacr4m/lispc-algorithms). This library will also include some implementations from the book, *Programming Algorithms in Lisp*). There is currently nothing under the data structures directory and I'm only working on the sorting module (located under `sorting/`) right now, meaning that most of the other subdirectories under the `algorithms/` directory are empty. The decision to write and develop the sorting module was mostly arbitrary. The sorting module currently includes the bubble sort, selection sort, insertion sort, shell sort, merge sort, and quick sort algorithms. More will be added as the project continues.

Alongside the sorting module, I'm also in the process of writing the animation module (located under `animate/`). Currently, the main priority is to create the animation module using the `ncurses` library (I'm aware that non-UNIX systems like Windows use different libraries, but that bridge will have to be crossed later). As of the moment, the animation module is a series of simple macros. I won't dwell on the macros since the idea was created in haste. The substitute for these animation macros is to use the `ncurses` library, dynamically changing the content on the user's screen to show the internal functionality of each algorithm and data structure. 

In the next post tomorrow, I will update the animation module and document the changes. This might be accompanied with miniscule refactoring also, but it will mostly detail the changes to the animation module.