---

---

I've recently started reading more from Knuth's Art of Computer Programming. Currently, I'm on the first book but I would like to mention a problem that I found interesting the other day:

> Suppose that we have a binary computer and a number $$x$$, $$1 \le x < 2$$. Show that the following algorithm, which uses only shifting, addition, and subtraction proportional to the number of places of accuracy desired, may be used to calculate an approximation $$y = \log_b x$$.
>
> ​	**L1.** [Initialize.] Set $$y \larr 0, z \larr x \text{ shifted right 1}, k \larr 1$$
>
> ​	**L2**. [Test for end.] If $$x = 1$$, stop.
>
> ​	**L3**. [Compare.] If $$x - z < 1$$, set $$z \larr z \text{ shifted right 1}, k \larr k + 1$$, and repeat this step.
>
> ​	**L4.** [Reduce.] Set $$x \larr x - z, z \larr x \text{ shifted right k }, y \larr y + \log_b(2^k/(2^k-1))$$, and go to L2.

I devised a crude proof as to why this algorithm calculates an approximation to $$y = \log_b x$$:

Firstly, if $$x = 1$$, then the algorithm immediately terminates at step $$L2$$ and $$y = 0$$ (the $$\log_b 1$$ = 0 for all positive integral $$b$$). 

