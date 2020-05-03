---

layout: post
title: Two Fundamental Theorems about Polynomials
date: 2020-05-02 8:16:00
summary: About the Factor Theorem and polynomials.
categories: math
---



Today I was reading a textbook and it was discussing about the use of partial fractions to facilitate integration in calculus. I remembered the technique of using partial fractions to write polynomials, and so I was a bit intrigued. I then came upon this statement:

> ...if two $n^{th}$ degree polynomials are equal for $n+1$ values of $x$, they are equal for all values of $x$.

I remembered this also, though in slightly different terms. Given a polynomial $f(x)$ of the $n^{th}$ degree, if the polynomial vanished for more than $n$ values of $x$, then the polynomial vanishes for all values of $x$. I sought to prove this to myself since I couldn't find it in the original textbook that I was reading.

To prove this, I thought of also proving another basic theorem that comes up in most algebra classes: the factor theorem. The factor theorem states that for any polynomial $f(x)$ that vanishes at $x = \alpha$, the polynomial is divisible by $x - \alpha$. 

Proving the factor theorem is quite simple:

Let $f(x) = px^n + qx^{n-1} + rx^{n-2} + ... + d$ for arbitrary real coefficients $p, q, r, ...$ and positive integral exponents. Then we are required to prove that if $f(a) = 0, x - a$ divides $f(x)$.

$$f(a) = pa^n + qa^{n-1} + ra^{n-2} + ... + d = 0$$

$$f(x) = px^n + qx^{n-1} + rx^{n-2} + ... + d$$

$$\therefore$$  $f(x) = p(x^n - a^n) + q(x^{n-1} - a^{n-1}) + ... + j(x - a)$ with $j$ being the last coefficient.

If the above expression divides $f(x)$, then it divides $x^n - a^n, x^{n-1} - a^{n-1}, ..., $ etc. 

Therefore, we must prove that for all $x^n - y^n$ with $n$ being a positive integer, $x -y$ divides $x^n - y^n$. The proof can be done by induction. For $n = 1$, $\frac{x - y}{x- y} = 1$ and for $n = 2$ the proposition also holds. Now assume that the proposition is true for  $1, 2, ..., n - 1$. Then we are required to prove that the proposition is true for $n$. If this is the case:

$$x^{n-1} - y^{n-1} = Q(x - y) \text{ for some } Q$$.

$$x^n - xy^{n-1} = Qx(x-y)$$

$$yx^{n-1} - y^n = Qy(x - y)$$ 

Adding both statements:

$$x^n - y^n + yx^{n-1} - xy^{n-1} = Q(x^2- y^2)$$

$$x^n - y^n + xy(x^{n-2} - y^{n-2}) = Q(x^2 - y^2)$$

$$x^n - y^n = Q(x^2 - y^2) - xy(x^{n-2} - y^{n-2})$$

Now, the first term on the right-hand side is obviously divisble by $x - y$ and the second term on the the right-hand side is also divisible by $x - y$ since $x^{n-2} - y^{n-2}$ is assumed to have been proven. Therefore, 

$$x^n - y^n = A(x - y)$$ where $A$ is the result of dividing the entire right-hand side by $x - y$. So, for positive integral $n$, the proposition is true that $x - y$ divides $x^n - y^n$. 

Therefore, the factor theorem is also true, since $x - a$ divides $x^n - a^n, x^{n-1} - a^{n-1}, ... x - a$. 

Now, we move onto the quote I mentioned in my calculus book. We are required to prove that $f(x) = px^n + qx^{n-1} + rx^{n-2} + ... + d$ vanishes for all values of $x$ if more than $n$ values cause the polynomial to vanish.

Using the factor theorem established previously, $f(x) = (x - \alpha)(x - \beta)(x - \gamma)...$ for $n$ values $\alpha, \beta, \gamma, ...$. With $n$ linear factors, suppose that $f(c) = 0$. Then, by the factor theorem, $x - c$ divides $f(x)$ or $(x - \alpha)(x - \beta)(x - \gamma)...$. However, if this is true, then that means that $(x - \alpha)(x - \beta)(x- \gamma)... = 0$ since that is the only way $x - c$ could divide it (remember that $x - c$ is not considered to be one of the $n$ roots, so there is no linear factor $x - c$ present in $(x - \alpha)(x - \beta)(x - \gamma)...$). Thus, the statement above is (albeit informally) proven since any value of $x$ will make the polynomial vanish.