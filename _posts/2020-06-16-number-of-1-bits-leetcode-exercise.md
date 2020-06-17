---
layout: post
title: Number of 1 Bits Leetcode Exercise
date: 2020-06-16 20:55
summary: Solution to Number of 1 Bits Leetcode Exercise.
categories: computer-science
---

Today I wanted to talk about a problem on Leetcode that I thought was interesting. The problem statement is as follows:

> Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the [Hamming weight](http://en.wikipedia.org/wiki/Hamming_weight)).

For example, the string `0000101010101` would  have a Hamming weight of 5 because it has 5 ones. My first incllination for solving this problem was to count the number of ones by shifting the binary number right by 1 and checking the digit in the unit's place:

```c++
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            if ((n & 1) == 1)
                count += 1;
            n >>= 1;
        }
        return count;
    }
};
```

This takes about 4 ms to run. However, a simple modification makes the program run almost instantly. The conditional statement in the loop is responsible for such substantial overhead. Generally speaking, most binary operations are instantaneous on modern computers, so trying to examine the digits without shifting, while it's possible, wouldn't change the run time by that much. Therefore, the conditional statement is definitely something worth eliminating. The way to do this is to recognize that binary numbers are composed of zeros and ones. As a result, we can just keep shifting `n`, adding the last digit to the `count` variable (since adding zero won't change the result):

```c++
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            count += (n & 1);
            n >>= 1;
        }
        return count;
    }
};
```

Surprisingly, this small change reduces the run time by a factor of 4, making it just as fast as Leetcode's proposed solution.