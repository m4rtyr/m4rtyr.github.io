---
layout: post
title: Why is a $- \times - = +$?
date: 2020-02-16 19:55:30
summary: One of the few pieces of mathematical knowledge we never learn the reasoning behind.
categories: mathematics
---



A negative times a negative is a positive. It's one of the few pieces of mathematical knowledge that's drilled into our brains in elementary school. Surprisingly, no explanation is provided as to why this is the case. Any curious student wanting to understand this counterintuitive result is met with silence. As we grow older, many of us don't really question the statement, and instead regard it as one of those "weird"  things in math. 

This property of numbers is not very difficult to understand. In fact, the proof is quite elegant, and requires essentially no algebra:


$$
-1 \times 1 = -1 \\
-1 \times (2 + (-1)) = -1 \\
(-1 \times 2) + (-1\times -1) = -1 \\
-2 + (-1 \times -1) = -1 \\
-1 \times -1 = 1 \\
\text{Q.E.D}
$$


The above "proof" is enough to show that a negative times negative is a positive since the negative of every positive integer $$a$$ is $$-1 \times a$$. However, there are some things that have not been established. For example, why is $-1 \times 1 = -1$ (more generally why is a negative times a *positive* a negative)? 

The answer to that question involves a proof similar to the one above:


$$
1 \times 1 = 1 \\
1 \times (2 + (-1)) = 1 \\
(1 \times 2) + (1 \times -1) = 1 \\
2 + (1 \times -1) = 1 \\
1 \times -1 = -1 \\
\text{Q.E.D}
$$




However, there are many operations here that are, from a rigorous perspective, undefined. What is the definition of $$\times$$? Why is the second statement equivalent to the third statement?  These questions might seem overly pedantic, but they're critical to the foundation of mathematics. How we define basic operations like $$=$$ or  $$+$$  or $$\times$$ affects the theorems developed in the rest of mathematics. An interesting demonstration of the failure to be pedantic is Russell's Paradox, which almost threatened to break the foundation of set theory, an important area of mathematics that is critical to number theory, probability, and boolean logic (the foundation of computer systems). Another amusing example is "dismal arithmetic" where multiplication and addition are defined as follows:


$$
a \times b = \min(a, b) \\
a + b = \max(a, b) \\
$$


The above definition is itself absurd and impractical, and also provides results that (while rather entertaining) are nonsensical. A final reason for why we need to be pedantic is because, according to Gödel's Incompleteness Theorem, mathematics cannot demonstrate its own consistency. This limitation makes it all the more necessary that the mathematical foundations we establish are secure, lest we end up with a system that is incoherent and that jeopardizes the advancement of "practical" science.

For all the operations in both proofs above to be well-defined, we can state the following axioms:

1. Zero is a natural number: $0 \in \mathbb N$.
2. Every natural number has a successor in the natural numbers: $\forall x \in \mathbb N\text{, } S(x) \in \mathbb N$. 
3. Zero is not the successor of any natural number: $\forall x \in \mathbb N \text{ } (0 \ne S(x))$.
4. If the successor of two natural numbers is the same, then the two original numbers are the same: $\forall x, y \in \mathbb N\text{, } \text{if }S(x) = S(y)\text{, } x = y$.
5. If a set contains zero and the successor of every number is in the set, then the set contains the natural numbers: $\forall V \subseteq \mathbb N, (0 \in \mathbb N) \text{ }\land\text{ } ((x \in V) \Rightarrow (S(x) \in V)) \Rightarrow V = \mathbb N$.

The above definitions were created by Giuseppe Peano in 1889 to provide a rigorous foundation for the natural numbers. Some clarifications are needed, however. Firstly, the equality operator has not been defined, some of the operations like $x = y$ undefined. For the sake of time, I won't define the equality operator here, but I have left its definition in the Notes section for further reading. Secondly, the successor of a number is a function that returns the successor of $x$. While we might be tempted to say that $S(x) = x + 1$, none of the above axioms define the $+$ operator. In fact, they don't define any of the common arithmetical operators. The definitions for $+, -, \times, \text{ and } \div$ is left to us. Therefore, it's up to us to define $+$ and $\times$. The following two sections are dedicated to that. 

## Addition

Addition can be defined as follows:

1. $\forall a \in \mathbb N,\text{ }a + 0 = a$
2. $\forall a, b \in \mathbb N, \text{ } a + S(b) = S(a + b)$ 

The first definition simply states that a number added to zero is itself. This definition is the basis for the next statement. Let's say I'm adding the natural numbers $5$ and $4$. To add $5$ and $4$ we can try to use (2) by noting that $4 = S(3)$. This gives the statement $5 + 4 = 5 + S(3) = S(5 + 3)$. However, we do not know the successor of $5 + 3$ or how to add $5$ to $3$ from just the above definitions. We can simplify $S(5 + 3)$ by noting that $S(2) = 3$. Therefore, $S(5 + 3) = S(5 + S(2))$. However, from (2), $5 + S(2) = S(5 + 2)$. Therefore, $S(5 + 3) = S(S(5 + 2))$. We can then continue to reapply (2) so that $S(5 + 3) = S(S(5 + 2)) = S(S(S(5 + 1))) = S(S(S(S(5))))$. In order to keep arithmetic simple, we generally avoid using the cumbersome nested notation above in favor of symbols for the natural numbers ($1, 2, 3, \text{etc}$). We assign the symbol $9 = S(S(S(S(5))))$. Therefore, $5 + 4 = 9$. It's easy to see how this can generalize so that we can always recursively define addition for any two natural numbers.

## Multiplication

Similarly to addition, we can provide the following definitions:

1. $\forall a \in \mathbb N, \text{ } a \times 0 = 0$
2. $\forall a, b \in \mathbb N, \text{ } a \times S(b) = a + (a \times b)$.

If we were to multiply the numbers $5$ and $4$, then:


$$
5 \times 4 \\
= 5 \times S(3) = 5 + (5 \times 3) \\
= 5 + (5 \times S(2)) = 5 + (5 + (5 \times 2)) \\
= 5 + (5 + (5 \times S(1))) = 5 + (5 + (5 + (5 \times 1))) \\
= 5 + (5 + (5 + (5 \times S(0))) = 5 + (5 + (5 + (5 + (5 \times 0)))) \\
= 5 + (5 + (5 + (5 + 0))) \\
= 20
$$


Again, instead of using nested $S$'s to write out natural numbers, we give them symbols (such as $20$ in the above problem).



The above is quite interesting but also clearly very long. We've established multiplication and addition but we've not established subtraction or division, and we haven't established the properties of commutativity, associativity, or distribution. Worse, we haven't even extended any of the above operations beyond the natural numbers! Therefore, $5 + (-3)$ is not defined and neither is $-3.1415 \times 1$. Axioms can be defined for $\mathbb Z$ (the integers), but it would be repetitive and monotonous to state them here. Instead, I've placed them in the Notes section for further reading. Either way, the Peano axioms are truly fascinating and brilliantly create a simple definition for some of the most common operations in mathematics.

## Notes



[1] [Britannica — Peano Axioms](https://www.britannica.com/science/Peano-axioms)

[2] [Mathematical Explanation of Peano Axioms](https://www2.hawaii.edu/~robertop/Courses/TMP/7_Peano_Axioms.pdf)

[3] [Russell's Paradox](https://plato.stanford.edu/entries/russell-paradox/)

[4] [Dismal Arithmetic (Simple Introduction)]( https://www.youtube.com/watch?v=cZkGeR9CWbk)

[5] [Dismal Arithmetic (Original Paper)]( https://cs.uwaterloo.ca/journals/JIS/VOL14/Sloane/carry2.pdf)

[6] [Brilliant — Peano Axioms](https://brilliant.org/wiki/peano-axioms/) 

[7] [Gödel's Incompleteness Theorem](https://plato.stanford.edu/entries/goedel-incompleteness/)

[8] [Axioms for Integers](https://www.math.ksu.edu/~cochrane/m511/m511axioms.pdf)

