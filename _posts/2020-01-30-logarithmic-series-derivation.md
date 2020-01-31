---
layout: post
title: Derivation of the Logarithmic Series 
date: 2020-01-30 12:39:25
summary: An explanation of how to derive $$ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} + ...$$
categories: math
---

I was working through one of my math textbooks and I came across the following derivation of the logarithmic series that I was a bit uncertain about at first:

> $$(1 + x)^y = 1 + y\ln(1 + x) + \frac{y^2}{2!}\{\ln(1 + x)\}^2 + \frac{y^3}{3!}\{\ln(1 + x)\}^3 + ... (1)$$
>
> By the Binomial theorem, when $$x < 1$$, we have
>
> $$(1 + x)^y = 1 + yx + \frac{y(y-1)}{2!}x^2 + \frac{y(y-1)(y-2)}{3!}x^3 + ... (2)$$
>
> Now in (2), the coefficient of $$y$$ is
>
>  $$x + \frac{-1}{1 \times 2}x^2 + \frac{(-1)(-2)}{1 \times 2 \times 3}x^3 + \frac{(-1)(-2)(-3)}{1 \times 2 \times 3 \times 4}x^4 + ... (3)$$
>
> That is, 
>
> $$x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + ...(4)$$
>
> Equate this to the coefficient of $$y$$ in (1); thus we have
>
> $$\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + ...$$

I wanted to expand this proof in my own words just to explain to myself the process they went through (and fill in the missing details).

**Proof** 

Essentially, the first part of the proof is obtained through the Exponential Theorem. The Exponential Theorem states:

$$a^x = 1 + x \ln a + \frac{(x \ln a)^2}{2!} + \frac{(x \ln a)^3}{3!} + ...$$

By substituting $$1 + x$$ for $$a$$ they obtain $$(1)$$. In order to obtain $$(2)$$ they just use the Binomial Theorem. The part that they skim over is how they acquire the "coefficient for $$y$$" and why we are even considering the coefficient of $$y$$ in the first place.

It's clear that $$(1)$$ and $$(2)$$ are equivalent expressions. Therefore, if we were to arrange $$(2)$$ so that its terms were in the form of $$Ky$$  just like in $$(1)$$ then we can merely *equate the coefficients* ($$K$$ and $$\ln (1 + x)$$) to obtain a formula for $$\ln (1 + x)$$. The reason we consider the coefficient of $$y$$ is because the coefficient of $$y^2$$, $$y^3$$, $$y^4$$, and in general $$y^n$$ in $$(2)$$ corresponds with the coefficients $$\biggl(\ln (1 + x)\biggl)^2$$ , $$ \biggl(\ln (1 + x)\biggl)^3$$, $$\biggl(\ln (1 + x)\biggl)^4$$, and in general $$\biggl(\ln (1 + x)\biggl)^n$$. Therefore, if we equated the coefficients, we would obtain a formula for $$\biggl(\ln (1 + x)\biggl)^n$$ and then have to take the $$n^{\text{th}}$$ root of the formula. This complicates the derivation; therefore, it's more desirable to find the coefficient of $$y$$ so then we can directly obtain the formula $$\biggl(\ln(1 + x)\biggl)$$. 

In order to rearrange $$(2)$$ like $$(1)$$, we need to expand $$(2)$$ in order to isolate $$y$$ and collect the terms. That is, 

$$(1 + x)^y = 1 + yx + \frac{y(y-1)}{2!}x^2 + \frac{y(y-1)(y-2)}{3!}x^3 + ... $$

$$(1 + x)^y = 1 + yx - \frac{x^2}{2!}y + \frac{2!x^3}{3!}y -  \frac{3!x^4}{4!}y + \frac{4!x^5}{5!}y + ... + y^2\biggl(...\biggl) + y^3\biggl(...\biggl) + y^4\biggl(...\biggl) + ...$$

In essence, we expanded each term and then organized it so that the terms containing $$y$$ were together and the terms containing higher powers of $$y$$ were separate. For example, the terms $$\frac{y(y-1)}{2!}x^2 = \frac{y^2 - y}{2!}x^2 = \frac{x^2}{2!}y^2 - \frac{x^2}{2!}y$$. Therefore, we can organize the expression so that the terms containing $$y$$ are on one side and the terms containing higher powers of $$y$$ are on another side.

From there, we can equate the coefficients, paying attention to $$y$$. Therefore, equating $$(1)$$ and our new form of $$(2)$$ above:

$$(1 + x)^y = 1 + y\ln(1 + x) + \frac{y^2}{2!}\{\ln(1 + x)\}^2 + \frac{y^3}{3!}\{\ln(1 + x)\}^3 + ... $$ 

$$= 1 + yx - \frac{x^2}{2!}y + \frac{2!x^3}{3!}y - \frac{3!x^4}{4!}y + \frac{4!x^5}{5!}y + \text{...} + y^2\biggl(...\biggl) + y^3\biggl(...\biggl) + y^4\biggl(...\biggl) + ...$$

$$ = 1 + y\biggl(x - \frac{x^2}{2} + \frac{2!x^3}{3!} - \frac{3!x^4}{4!} + \frac{4!x^5}{5!} + \text{...} \biggl) + y^2\biggl(...\biggl) + y^3\biggl(...\biggl) + y^4\biggl(...\biggl) + ...$$

$$\therefore$$ if we equate the coefficients of $$y$$ in both equations then we get

$$\ln (1 + x) = x - \frac{x^2}{2} + \frac{2!x^3}{3!} - \frac{3!x^4}{4!} + \frac{4!x^5}{5!} + ...$$ 

**Q.E.D**

I know this post might not be satisfactory for some (especially those who prefer absolute rigor in mathematics), and I also know that this explanation might not suffice for most people (it's mostly for myself anyway), so I decided to give some information below that could be useful.

## Notes

[1] — The original derivation comes from Henry Sinclair and S.R Knight's [*Higher Algebra: A sequel to Elementary Algebra for Schools*](https://archive.org/details/higheralgebraseq00hall/page/n5/mode/2up). 

[2] — This explanation was based on [a question I asked](https://math.stackexchange.com/questions/3526553/explanation-of-this-derivation-of-the-logarithmic-series) on the Mathematics StackExchange. 



