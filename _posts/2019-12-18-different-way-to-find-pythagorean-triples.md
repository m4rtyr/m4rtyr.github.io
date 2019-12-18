---
layout: post
title: Generating Pythagorean Triples Given their Sum
date: 2019-12-18 12:34:23
summary: An interesting way to find Pythagorean triples.
categories: math computer-science
---

Recently, I started solving some problems on Project Euler which is "*a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve.*"

I've solved only a few problems, but there's one particular one that I thought was
quite interesting:


> A Pythagorean triplet is a set of three natural numbers, $$a < b < c$$, for which,
> $$a^2 + b^2 = c^2$$
>
> For example, $$3^2 + 4^2 = 9 + 16 = 25 = 5^2$$.
>
> There exists exactly one Pythagorean triplet for which $$a + b + c = 1000$$.
> Find the product $$abc$$.

My approach initially was to take a look at a list of Pythagorean triples and see
if I can decipher some pattern. After a bit of toiling around, I noticed that there
are many triples where $$c$$ is only one more than $$b$$, i.e, $$c = b + 1$$:

$$\begin{align}
  3^2 + 4^2 & = 5^2 \\
  9^2 + 40^2 & = 41^2 \\
  5^2 + 12^2 & = 13^2 \\
  7^2 + 24^2 & = 25^2 \\
\end{align}$$

From the above, we get the following formula:

$$\begin{align}
  a^2 + b^2 & = (b + 1)^2 \\
  a^2 & = b^2 + 2b + 1 - b^2 \\
  a^2 & = 2b + 1
\end{align}$$

From there, we plug $$a = \sqrt{2b+1}$$ and $$c = b+1$$ into $$a + b + c = n$$
where $$n$$ is any arbitrary positive integer (I do this to make the formula more general).

$$\begin{align}
\sqrt{2b+1} + b + b + 1 & = n \\
\sqrt{2b+1} + 2b + 1 & = n \\
\sqrt{2b + 1} & = n-2b-1 \\
2b + 1 & = \bigg(n - (2b + 1)\bigg)^2 \\
a^2 & = \bigg(n - a^2\bigg)^2 \\
n - a^2 & = a \\
a^2 + a & = n \\
\biggl(a + \frac{1}{2}\biggl)^2 & = n + \frac{1}{4} \\
a & = \sqrt{n + \frac{1}{4}} - \frac{1}{2}
\end{align}$$

...And that's it! We've devised a formula for $$a$$ in terms of $$n$$. Therefore,
if we plug in $$1000$$ in for $$n$$, then we get:

$$\begin{align}
& \sqrt{1000 + \frac{1}{4}} - \frac{1}{2} \\
& \sqrt{\frac{4001}{4}} - \frac{1}{2} \\
& \frac{\sqrt{4001} - 1}{2} \\
\end{align}$$

The $$\sqrt{4001}$$ is not a perfect square, meaning that $$a$$ is not an integer.
Therefore, there is no Pythagorean triple such that $$a + b + c = 1000$$ and
$$c$$ is one more than $$b$$.

At this point, this approach may seem hopeless. We have no answer. However, I thought,
what if instead of spacing $$b$$ and $$c$$ to be one apart, I spaced them to be $$2$$ apart,
or $$3$$ apart, or $$s$$ apart?

Thus, we go through the same process, except this time $$c = b + s$$. Additionally, this time $$a^2 = 2bs + s^2$$.

$$\begin{align}
\sqrt{2bs + s^2} + b + b + s & = n \\
\sqrt{2bs + s^2} + 2b + s & = n \\
\sqrt{2bs + s^2} & = n - 2b - s \\
2bs + s^2 & = \biggl(n - (2b + s)\biggl)^2 \\
a^2 & = \biggl(n - \frac{a^2}{s}\biggl)^2 \\
n - \frac{a^2}{s} & = a \\
\frac{a^2}{s} + a & = n \\
a^2 + sa & = ns \\
\biggl(a + \frac{s}{2}\biggl)^2 & = ns + \frac{s^2}{4} \\
a & = \sqrt{ns + \frac{s^2}{4}} - \frac{s}{2} \\
\end{align}$$

Whew! We finally have a formula for generating $$a$$ given a spacing $$s$$ between
$$b$$ and $$c$$. When we tried $$s = 1$$, we saw that $$a$$ was not an integer.
Therefore, if we try $$s$$ for multiple integer values, then we should be able
to (at some point) find the answer. So, given that $$n = 1000$$, we must generate
multiple integer values for $$s$$ until we acquire an integer answer for $$a$$.

Of course, I'm not going to sit here all day plugging in values for $$s$$ by hand.
Why not have a computer program do it for me? Below is some simple code in Go
that generates multiple values for $$s$$ given a certain $$n$$:

    func main() {
      n := 1000.0
      for i := 1; i <= 100; i++ {
        s := float64(i)
        val := fmt.Sprintf("%f", math.Sqrt(n*s + s*s/4) - s/2)
        val2 := fmt.Sprintf("%f", s)
        fmt.Println("s: " +  val2 + " " + val)
      }
    }


I selected $$100$$ arbitrarily as the limit for $$s$$. Coincidentally, however,
the solution is within this range! For $$s = 50$$, we get $$a = 200$$. Therefore,

$$\begin{align}
& 200^2 + 375^2 = 425^2 \\
& 200 \times 375 \times 425 = 31875000
\end{align}$$
