---
layout: post
title: An Example of Induction and Direct Method of Proof
date: 2020-05-16 21:16:00
summary: An example of induction and direct method of proof of $8^n - 3^n \equiv 0 \pmod 5$
categories: mathematics
---



Today I came across the following problem and I wanted to write a solution for it:



> Prove $8^n - 3^n$ is divisible by 5 for all positive integer $n$.

This proof is pretty simple but I wanted to show two ways to do it.



**Method 1: Induction**

This might seem pretty natural at first. Essentially, we need to prove a base case and then show that the proposition holds for any given $n$.



Therefore, let $f(n) = 8^n - 3^n$. For $f(1) = 8 - 3 = 5$. Therefore, the proposition is true for the case $n = 1$. Now assume that the proposition is true for $1, 2, 3, ..., n-1$. We are now required to prove that the proposition holds for $n$. The following proves that the proposition holds for $n$:



$$f(n-1) = 8^{n-1} - 3^{n-1}$$

$$8f(n-1) = 8^n - 8(3^{n-1})$$

$$3f(n-1) = 3(8^{n-1}) - 3^n$$

Now, sum (2) and (3) to obtain:

$$8^n - 3^n + 3(8^{n-1}) - 8(3^{n-1}) = 11f(n-1)$$

$$8^n - 3^n + 24\biggl(8^{n-2} - 3^{n-2}\biggl) = 11f(n-1)$$

At this point, the right hand side is divisible by $5$ since by hypothesis we know that $f(n-1)$ is divisible by $5$. Additionally, $24\biggl(8^{n-2} - 3^{n-2}\biggl)$ is also divisible by $5$ (the case for $n-2$ is also proven by hypothesis). Therefore, these terms are divisible by $5$ that means that $8^n - 3^n$ is also divisible by $5$. 

**Method 2: Direct**

This one is more elegant in my opinion. The following is the proof:

$$8^n - 3^n$$

$$ = (5 + 3)^n - 3^n$$

$$= \sum_{r=0}^n (^nC_r\text{ }5^r \cdot 3^{n-r}) -3^n$$

$$= \sum_{r=1}^n(^nC_r\text{ }5^r \cdot 3^{n-r})$$

$$= 5\sum_{r=1}^n(^nC_r\text{ }5^{r-1} \cdot 3^{n-r})$$

Therefore, the expression is divisible by $5$.
