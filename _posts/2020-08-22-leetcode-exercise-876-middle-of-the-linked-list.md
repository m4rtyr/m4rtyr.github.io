---
layout: post
title: Leetcode Exercise 876. Middle of the Linked List
category: computer-science
tags: competitive-programming leetcode c++
use_math: true
excerpt_separator: <!--eof-->
---

<!--eof-->

## Problem

> Given a non-empty, singly linked list with head node `head`, return a middle node of linked list.
>
> If there are two middle nodes, return the second middle node.

## Code

I came up with the following solution in C++ to the problem:

```c++
ListNode* middleNode(ListNode* head) {
  ListNode *fast = head, *slow = head;
  while (fast && fast->next) {
      fast = fast->next->next;
      slow = slow->next;
  }
  return slow;
}
```

​	The algorithm above uses two pointers, a `slow` pointer and a `fast` pointer. The `fast` pointer moves twice as fast as the `slow` pointer. Below I'll explain why the algorithm works.

## Explanation

​	The input we are given is a non-empty, singly linked list. We must show that the algorithm finds the middle node for all non-empty singly linked lists. A linked list can have an odd length or and even length. If the list has an odd length, that means there is exactly one node in the middle. If the list has an even length, then there are two nodes in the middle and we are required to return the second one.

​	Let's first consider the odd case. Let's assume there are $2m+1$ nodes where $m$ is a positive integer. Both pointers start at node $1$. After the first iteration, the `fast` pointer is at node $3$ and the `slow` pointer is at node $2$. After the second iteration, the `fast` pointer is at node $5$ and the `slow` pointer is at node $3$. After the third iteration, the `fast` pointer is at node $7$ and the `slow` pointer is at node $4$. Let's place the values in a table to understand the trend.

| `fast` position | `slow` position | iteration |
| --------------- | --------------- | --------- |
| 1               | 1               | 0         |
| 3               | 2               | 1         |
| 5               | 3               | 2         |
| 7               | 4               | 3         |
| 9               | 5               | 4         |
| 11              | 6               | 5         |
| 13              | 7               | 6         |
| 15              | 8               | 7         |
| 17              | 9               | 8         |

​	If you notice, the `fast` pointer has position $2*(\text{position of slow pointer}) - 1$. Thus, when the `slow` pointer is at the middle of the list (position $m+1$) the `fast` pointer is at position $2*(m+1) - 1 = 2m + 1$. So, if the `fast` pointer moves at twice the speed of the `slow` pointer, then the `slow` pointer will point to the middle node by the time the `fast` pointer arrives at the end of the list. 

​	On a similar vein, we can prove that this algorithm works for an even length list. Let there be $2m$ nodes. Since the pattern is the exact same, we determine that when the `slow` pointer arrives at the position $m+1$ (the second middle node), the `fast` pointer is at position $2*(m+1) - 1 = 2m + 1$. However, since there are only $2m$ positions, that means that the `fast` pointer has already finished traversing the entire list (`NULL`). Thus, the code above still works and the algorithm solves the problem. 