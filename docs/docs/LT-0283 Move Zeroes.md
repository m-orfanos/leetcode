---
tags:
- difficulty/easy
- topics/array
- topics/two-pointers
---

# 0283 Move Zeroes

<https://leetcode.com/problems/move-zeroes>

## Description

- Problem description
    - Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.
    - Note that you must do this in-place without making a copy of the array.
- Constraints:
    - $1 <= nums.length <= 10^4$
    - $-2^{31} <= nums[i] <= 2^{31} - 1$
- Examples
    - Example 1
        - Input: `nums = [0,1,0,3,12]`
        - Output: `[1,3,12,0,0]`
    - Example 2
        - Input: `nums = [0]`
        - Output: `[0]`
- Follow up
    - Could you minimise the total number of operations done?

## Solutions

### Use built-in sort with custom comparator

```python
def move_zeroes(nums: List[int]) -> None:
    def zeros_are_massive(a: int, b: int) -> int:
        if a == 0:
            return sys.maxsize - b
        if b == 0:
            return a - sys.maxsize
        else:
            return 0
            
    nums.sort(key=cmp_to_key(zeros_are_massive))
```

Time complexity: $O(n*log(n))$
Space complexity: $O(n)$

### Create temporary copy of valid numbers and fill remaining

```python
def move_zeroes(xs: List[int]) -> None:
    tmp = []
    for i in range(len(xs)):
        if xs[i] != 0:
            tmp.append(xs[i])

    for i in range(len(tmp)):
        xs[i] = tmp[i]

    for i in range(len(xs) - len(tmp)):
        xs[len(xs) - 1 - i] = 0
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Push the snowball

A nice solution shared by someone on leetcode.

```python
def move_zeroes(xs: List[int]) -> None:
    snowball_size = 0
    for i in range(len(xs)):
        if xs[i] == 0:
            snowball_size += 1
        elif snowball_size > 0:
            tmp = xs[i]
            xs[i] = 0
            xs[i - snowball_size] = tmp
```

Time complexity: $O(n)$
Space complexity: $O(1)$

### One-pass, two-pointer iterative approach

"two pointers" is actually the indices
i, regular index used to iterate over list
j, index of the next non-zero element
basically push all elements down
need to fill in zeros when done

```python
def move_zeroes(xs: List[int]) -> None:
    j = 0
    for i in range(len(xs)):
        if xs[i] != 0:
            xs[j] = xs[i]
            j += 1
            
    # set remaining values to zeroes
    for i in range(j, len(xs)):
        xs[i] = 0
```

Time complexity: $O(n)$
Space complexity: $O(1)$
