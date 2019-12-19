---
layout: post
title: Recursive Digit Reversal Formula
date: 2019-12-19 15:23:45
summary: A mathematical formula for reversing digits
categories: math computer-science
---

I derived this formula in middle school, and for years it has been buried in
countless notebooks. I wanted a permanent place to put it.

## Digit Reversal Formula for 2 Digit Numbers

How do we reverse two digit numbers with a mathematical formula? We can think of the problem by considering
a hypothetical two-digit number $$AB$$ (not $$A \times B$$; these are just two-digits
that are put next to each other. I'll use this convention for the rest of the article).

If we want to reverse this number so that we get $$BA$$, then we can exploit the
following properties. Firstly, $$AB = 10A + B$$ and $$BA = 10B + A$$. Basically,
this means we have to isolate $$A$$ by removing $$B$$ and dividing by $$10$$. Once
we have $$A$$, we can obtain $$B$$ by subtracting $$10A$$ from $$AB$$. Then, we plug
the values of $$B$$ and $$A$$ into the formula $$10B + A$$ to get $$BA$$.

That's a mouthful. Let's try to put that in mathematical language. To obtain $$A$$,
we first need to subtract $$B$$ from $$AB$$. To get the value $$B$$ independently, we
can use the modulus operator. Therefore, if we have a two-digit number $$p = AB$$
then we can acquire the value of $$B$$ independently like so:

$$\begin{equation}
B = p\pmod{10}
\end{equation}$$

Now we can acquire $$A$$. We subtract $$B$$ from $$AB$$. That is,

$$\begin{equation}
AB - B = p - \bigg(p\mod{10}\bigg)
\end{equation}$$

Then we divide by 10:

$$\begin{align}
AB - B & = A0 = p - \bigg(p\mod{10}\bigg) \\
A = A0 \div 10 & = \frac{p - \bigg(p\mod{10}\bigg)}{10}
\end{align}$$

Now that we have the values of $$B$$ and $$A$$, we plug those into the expression
$$10B + A$$ and get the formula to obtain $$BA$$:

$$\begin{align}
10B + A & = 10\biggr(p\mod{10}\biggr) + A \\
& = 10\Biggr(p\mod{10}\Biggr) + \frac{p - \bigg(p\mod{10}\bigg)}{10} \\
& = \frac{100\Biggr(p\mod{10}\Biggr)}{10} + \frac{p - \bigg(p\mod{10}\bigg)}{10} \\
& = \frac{p + 99\biggl(p\mod{10}\biggl)}{10}
\end{align}$$

## Digit Reversal Formula for $$n$$ Digit Numbers

You might be wondering how this can be extended. While we have created a formula
for two-digit numbers, this doesn't necessarily mean that we can extend this to three-digits.
It seems as if, each time, we'll have to create a new formula for every digit.

The reality is that we can implement a *function* that will output a number with its
digits reversed without having to create a new formula each time. Think of the two-digit
reversal formula as a function $$R_2(p)$$  where $$p$$ is any two-digit number. Now, let's
look at an example of a three-digit number we want to reverse:

$$342 \rightarrow \text{?} \rightarrow 243$$

To do this, we can think of the digits $$42$$ as being a two-digit number embedded within
the three-digit number $$342$$. Therefore, if we can isolate $$42$$ from $$3$$, then we
can apply $$R_2(42)$$ to get $$24$$. We can proceed to isolate $$3$$ by subtracting $$42$$
from $$342$$ and then dividing by $$100$$. Then, we can append $$3$$ to the end of $$240$$
(we get $$240$$ by taking $$R_2(42)$$ and multiplying it by $$10$$ to create an extra place for
the $$3$$).

Let's illustrate this mathematically. Let's assume we have a number $$p = ABC$$. Then, we can acquire
$$BC$$ using modular arithmetic:

$$\begin{align}
BC = p\pmod{100}
\end{align}$$

Then, subtract $$BC$$ from $$ABC$$ to get $$A00$$. Isolate $$A$$ by dividing by $$100$$:

$$\begin{align}
ABC - BC & = A00 = p - \biggl(p\mod{100}\biggl) \\
A = A00 \div 100 & = \frac{p - \biggl(p\mod{100}\biggl)}{100}
\end{align}$$

Now that we have isolated $$BC$$ and $$A$$, we can use $$R_2$$ to reverse $$BC$$,
and then add $$A$$ at the end like so;

$$\begin{align}
10BC + A & = 10\Biggr(R_2\biggl(p\mod{100}\biggl)\Biggr) + A \\
& = 10\Biggr(R_2\biggl(p\mod{100}\biggl)\Biggr) + \frac{p - \biggl(p\mod{100}\biggl)}{100}
\end{align}$$

Now, if you think about it, there's a pattern here. Let's say I have the number
$$123456789...$$ and so on and so forth. If I reverse all the digits after the first $$1$$,
and then append the $$1$$ at the end, I get the reversed number. In essence, I can define a function
$$R_n$$ for reversing $$n$$-digit numbers recursively in terms of $$R_{n-1}$$.

Mathematically,

$$\begin{align}
R_n = 10\Biggr(R_{n-1}\biggl(p\mod{10^{n-1}}\biggl)\Biggr) + \frac{p - \biggl(p\mod{10^{n-1}}\biggl)}{10^{n-1}}
\end{align}$$

We want to define this for $$n > 2$$ since for $$n = 2$$ we have a formula. The formula
doesn't work for $$n = 1$$\*. Therefore,


$$R_n = \begin{cases}
10\Biggr(R_{n-1}\biggl(p\mod{10^{n-1}}\biggl)\Biggr) + \frac{p - \biggl(p\mod{10^{n-1}}\biggl)}{10^{n-1}}
\text{ if } n > 2 \\
\\
\\
\frac{p \text{ + } \text{ 99 }\biggl(p\mod{10}\biggl)}{10} \text{ if } n = 2
\end{cases}$$

<sup><sub>\* The formula "doesn't work" in the sense that if you do $$R_2(1)$$,
you get $$10$$. This may work well if the term "digit reversal" is defined differently.
For our purposes, we won't define digital reversal this way. </sub></sup>
