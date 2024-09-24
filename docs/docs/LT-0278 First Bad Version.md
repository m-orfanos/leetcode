---
tags:
- difficulty/easy
- topics/binary-search
- topics/interactive
---

# 0278 First Bad Version

<https://leetcode.com/problems/first-bad-version>

## Description

- Problem statement
    - You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
    - Suppose you have n versions `[1, 2, …, n]` and you want to find out the first bad one, which causes all the following ones to be bad.
    - You are given an API `bool isBadVersion(version)` which returns whether version is bad. Implement a function to find the first bad version. You should minimise the number of calls to the API.
- Constraints
    - $1 <= bad <= n <= 2^{31} - 1$
- Examples
    - Example 1
        - Input: `n = 5`, `bad = 4`
        - Output: `4`
    - Example 2
        - Input: `n = 1`, `bad = 1`
        - Output: `1`

## Solutions

### Linear search

check version starting from 1
stop when you hit the first bad version

Time complexity: $O(n)$
Space complexity: $O(1)$

### Modified Binary Search

squeeze from both sides, begin with low=1 and high=n
stop when `high<low`

notation used in the example

```text
G = good version
B = bad version

12345 = the versions written side-by-side

The rows 1, 2 and 3 above denote iterations of the binary search loop.

L = low
H = high
M = mid = low + (high-low)//2

L, M, and H are all integers
```

example 1

```text
     GGGBB
     12345
  1  L-M-H
  2     LH  L=M
  3    HL   loop exits before run
```

example 2

```text
     GBBBB
     12345
  1  L-M-H
  2  LH    L=M
  3   |    L=M=H
  4  HL    loop exits before run
```

note `low` always contains the target version

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def first_bad_version(
    n: int,
    isBadVersion: Callable[[int], bool]
) -> int:
    low = 1
    high = n
    while low <= high:
        mid = low + (high - low) // 2
        if isBadVersion(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low
```

Time complexity: $O(log(n))$
Space complexity: $O(1)$
