---
layout: post
title: What are pointers? 
date: 2020-01-30 12:39:25
summary: An in-depth explanation of pointers and how they work.
categories: computer-science programming
---



The concept of a pointer is often misunderstood because of the fact that it's not explained rigorously and because they can introduce a level of complexity that perplexes the programmers. While pointers are generally associated with the C programming language (and that's the language I will be writing and talking about today), pointers are also implemented in Go and in Rust (though Rust utilizes raw pointers to a much lesser degree and Go explicitly forbids pointer arithmetic). 

For myself and for others, I thought I would explain the concept of a pointer. 

## What is a Pointer?

A pointer is a variable that stores the memory address of a variable. A *memory address* is just a reference to a location in memory, usually represented by a number in hexadecimal. In order to think about pointers, it's critical to have a mental model to visualize how memory is organized. In most machines, memory is organized as a linear array of consecutively numbered memory cells that can be manipulated and accessed individually or in groups. 

Now consider the declaration of the following pointer variable:

`int *p;`

The above code merely creates a pointer to an integer, and names this pointer `p`. The pointer contains the address of an integer that's located in the machine's memory. For example, `p` might contain the memory address `0x1234` or `0x54f32` or another number that represents a location in the machine's memory. Currently, `p` does not point to any integer in particular. It's important to note that the pointer contains only the memory address of an integer, not the actual integer itself. The actual integer is stored inside the memory address.

How can we access the integer inside the memory address? In the C programming language, we can access the contents of a memory address by *dereferencing* the pointer with the `*` operator:

`printf("%d\n", *p);`

The `*` operator conceptually does the following when applied to the pointer: it examines the memory address stored in the pointer variable, goes to that memory address, and then reads off the data at that memory address and returns it. In this case, the data is handed as an argument to the `printf` function.

In order to create a pointer to a variable, we need to get the memory address of the variable. How do we do that? In C, we can obtain a *reference* to the variable by using the `&` operator like so:

```c
int v = 5;
int *p = &v; // &v returns the memory address of the integer stored in variable v
```

Before moving on to more complex operations on pointers, it's critical to discuss one thing: if a pointer variable just holds a memory address, then when we dereference the pointer how does the program read off the appropriate amount of memory?

For example, let's say we declared a generic type in C like follows:

```c
int v = 5;
// In this case, the pointer has void type, so we don't know the type of data stored.
void *q = &v; 
printf("%d\n", *q);
```

`q` only holds the memory address of `v`, but it doesn't know the type of `v`. So, when it's dereferenced in line 4, how does it know to read off only as much memory as is needed to store an integer (4 bytes)? If you run the code above you will get a compilation error. This is because the program *doesn't* know how much to read. It only knows the memory address, but it doesn't know the type. Therefore, the program cannot be sure how much data to read off. If, instead, we declared `q` has a pointer to an integer, then the program would only read the amount of memory necessary to store an integer. Similarly, if `q` was a pointer to a `char`, it would only read the amount of memory necessary to store a `char` (1 byte).

In summary, a pointer is just a variable that stores a memory address, and by using the `*` and `&` operators we can respectively obtain the data pointed to by a pointer and obtain the memory address of a variable.