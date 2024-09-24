---
tags:
- difficulty/easy
- topics/array
- topics/hash-table
---

# 0001 Two Sum

<https://leetcode.com/problems/two-sum>

## Description

- Problem statement
    - Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
    - You may assume that each input would have exactly one solution, and you may not use the same element twice.
    - You can return the answer in any order.
    - Only one valid answer (pair) exists.
- Follow-up
    - Can you come up with an algorithm that is less than $O(n^2)$ time complexity?
- Constraints
    - $2 <= nums.length <= 10^4$
    - $-10^9 <= nums[i] <= 10^9$
    - $-10^9 <= target <= 10^9$
- Examples
    - Example 1
        - Inputs: $nums = [2,7,11,15]$, $target = 9$
        - Output: $[0,1]$
    - Example 2
        - Inputs: $nums = [3,2,4]$, $target = 6$
        - Output: $[1,2]$
    - Example 3
        - Inputs: $nums = [3,3]$, $target = 6$
        - Output: $[0,1]$

## Solutions

### Solution 1: nested for-loop search (brute-force approach)

```text
nums   = [2,7,11,15]
target = 9
```

Can check all pairs of elements until a match is found.
There are (`4 choose 2`) 6 unique pairs.

|  i  |  j  | unique pair |          sum |
|:---:|:---:|:-----------:| ------------:|
|  0  |  0  |     ❌      |            - |
|  0  |  1  |     ✅      |    2 + 7 = 9 |
|  0  |  2  |     ✅      |  2 + 11 = 13 |
|  0  |  3  |     ✅      |  2 + 15 = 17 |
|  ~  |  ~  |      ~      |            ~ |
|  1  |  0  |     ❌      |            - |
|  1  |  1  |     ❌      |            - |
|  1  |  2  |     ✅      |  7 + 11 = 18 |
|  1  |  3  |     ✅      |  7 + 15 = 22 |
|  ~  |  ~  |      ~      |            ~ |
|  2  |  0  |     ❌      |            - |
|  2  |  1  |     ❌      |            - |
|  2  |  2  |     ❌      |            - |
|  2  |  3  |     ✅      | 11 + 15 = 27 |
|  ~  |  ~  |      ~      |            ~ |
|  3  |  0  |     ❌      |            - |
|  3  |  1  |     ❌      |            - |
|  3  |  2  |     ❌      |            - |
|  3  |  3  |     ❌      |            - |

alternative view

| i \ j |  0  |  1  |  2  |  3  |
| -----:|:---:|:---:|:---:|:---:|
|     0 | ❌  | ✅  | ✅  | ✅  |
|     1 | ❌  | ❌  | ✅  | ✅  |
|     2 | ❌  | ❌  | ❌  | ✅  |
|     3 | ❌  | ❌  | ❌  | ❌  |

Can create pairs using nested for-loops.

```python
def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

Alternatively, can use built-in language functionality to create the pairs (if available). If using python, that's `itertools.combinations`.

Time complexity: $O(n^2)$
Space complexity: $O(1)$

### Solution 2: single-pass search

```text
nums   = [2,7,11,15]
target = 9
```

How to avoid checking all pairs?

Rewrite `arr[i] + arr[j] = 9` as `n = 9 - arr[i]`.
The question becomes: does `n` exist in the array?

Can transform and sort the array while keeping track of the original indices.
Then use binary search to find if the value exists.
(Note: in the example below the array is already sorted but that's not always the case).
(Note: Code not shown.)

```text
nums   = [2,7,11,15]
nums'  = [(2,0), (7,1), (11,2), (15,3)]
target = 9

# need to check against the first element in the tuple
modified_binary_search(nums', 9-2)
```

A better choice is to use a hash-map (dictionary).

```text
nums   = [2,7,11,15]
nums'  = { 
    2:0,
    7:1,
    11:2,
    15:3,
}
target = 9

nums'[9-2] => nums'[7] => 1
```

in code,

```python
def two_sum(nums: List[int], target: int) -> List[int]:
    nums_dict = {n: i for (i, n) in enumerate(nums)}
    for i, n in enumerate(nums):
        m = target - n
        if m in nums_dict and nums_dict[m] != i:
            return [i, nums_dict[m]]
    return []
```

Time complexity: $O(n)$
Space complexity: $O(n)$
