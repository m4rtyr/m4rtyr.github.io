---

layout: post
title: Removing Duplicates
date: 2020-05-09 14:40:00
summary: Removing duplicates from an array in $O(1)$ space and $O(N)$ time complexity.
categories: computer-science programming
---


I was solving some algorithm problems and I came across this question:

> Given a sorted array *nums*, remove the duplicates in-place such that each element only appears once and return the new length. Do not allocate extra space for another array, you must do this modifying the input array with $O(1)$ extra memory.



I ended up solving the problem like this (in Golang):

```go
func removeDuplicates(nums []int) int {
    k := 0
    for i := 0; i < len(nums); i++ {
        j := i
        for j < len(nums)-1 && nums[j] == nums[j+1] {
            j += 1
        }
        tmp := nums[j]
        nums[j] = nums[k]
        nums[k] = tmp
        k += 1
        i = j
    }
    return k
}
```

Basically, the `j` pointer traverses through the array while a duplicate is present. Once `nums[j] != nums[j+1]`, `nums[j]` is exchanged with `nums[k]` where `k = 0` and is incremented each time in the loop to indicate the size. Then `i` is set to `j` and then incremented in the for loop so `i` starts on `j+1` in the next pass. This approach basically tries to skip the duplicates and, once the chain of duplicates stop, place the first instance of the integer in the array by swapping, relegating the duplicates to the back of the array. The above solution uses $O(1)$ space but takes $O(N^2)$ time (in the worst case, the entire array is just one integer duplicated many times).



The solution given on Leetcode was this (in Java):

```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
```

This solution is quite clever. Basically it uses the technique of a fast and slow pointer. In this case, the fast pointer is `j` and the slow pointer is `i`. Essentially, it marks the number at the beginning with `i`, and then continually increments `j` while `nums[j] = nums[i]`. Once the duplicate chain is finished, it increments `i` to the next index and assigns `nums[i]` to `nums[j]` (unlike my solution, `nums[j]` cannot ever equal `nums[i]` Not only is my solution $O(N^2)$ time but it actually makes many redundant passes. If you try my solution on the array $[1, 1, 2]$ it takes two passes to go through the array before swapping two different values). Once the pass through the array is finished, the index that $i$ is on needs to be incremented by one to give the length of the array.

