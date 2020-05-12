---

layout: post
title: Disappeared Numbers
date: 2020-05-11 21:16:00
summary: A solution to Disappeared Numbers Leetcode Problem
categories: computer-science programming
---

I was on Leetcode solving some problems and I found this one that I thought was quite interesting:

> Given an array of integers where 1 ≤ a[i] ≤ *n* (*n* = size of array), some elements appear twice and others appear once.
>
> Find all the elements of [1, *n*] inclusive that do not appear in this array.



I thought the problem was quite interesting, so I tried the problem using extra memory at first. Here's my solution:

```go
func findDisappearedNumbers(nums []int) []int {
    var disappeared []int
    var buckets = make([]int, len(nums))
    for i := 0; i < len(nums); i++ {
        buckets[nums[i]-1] += 1
    }
    for i := 0; i < len(buckets); i++ {
        if buckets[i] == 0 {
            disappeared = append(disappeared, i+1)
        }
    }
    return disappeared
}

```

It's pretty simple. Since each number is between $1$ and $n$, we can create a list (that I call `buckets`) to store the counts of each number. As we loop through the array, we look at the number and update its corresponding index in the `buckets` array. Then, we loop over the array again and append all numbers that appear $0$ times in the array.

To do this without extra space, I had to think for a little while. Eventually, I came up with a solution:

```go
func findDisappearedNumbers(nums []int) []int {
    var disappeared []int
    for i := 0; i < len(nums); i++ {
        for nums[i] != 0 && nums[nums[i]-1] != 0 {
            index := nums[i]-1
            nums[i] = nums[index]
            nums[index] = 0
        }
    }
    
    for i := 0; i < len(nums); i++ {
        if nums[i] > 0 {
            disappeared = append(disappeared, i+1)
        }
    }
    return disappeared
}
```

This solution is a little more complicated than the above but not very difficult to understand. Essentially, whenever we come upon a number in the array, we check its corresponding index. We mark the corresponding index with $0$ to indicate that it was visited, and take the element in the corresponding index and place it into the current index. We repeatedly do this until we have went through the entire array.

If an index is not zeroed out, that means that that index, when we add one to it, is a disappeared number. This solution uses 100% less space but is only 80.19% faster. There's a faster solution which involves something similar to what I'm doing, but it's [more clever](https://www.youtube.com/watch?v=CTBEcmzLAuA&feature=youtu.be).