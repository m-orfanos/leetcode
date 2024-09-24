---
tags:
- difficulty/easy
- topics/dynamic-programming
- topics/bit-manipulation
---

# 0338 Counting Bits

<https://leetcode.com/problems/counting-bits>

## Description

- Problem statement
    - Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` `(0 <= i <= n)`, `ans[i]` is the number of `1`'s in the binary representation of `i`.
- Constraints
    - $0 <= n <= 10^5$
- Examples
    - Example 1
        - Input: `n = 2`
        - Output: `[0,1,1]`
    - Example 2
        - Input: `n = 5`
        - Output: `[0,1,1,2,1,2]`
- Follow up
    - It is very easy to come up with a solution with a runtime of $O(n*log(n))$. Can you do it in linear time $O(n)$ and possibly in a single pass?
    - Can you do it without using any built-in function (i.e., like `__builtin_popcount` in C++)?

## Solutions

### Keep running count while converting base 10 to base 2

```python
def count_bits(n: int) -> List[int]:
    def nb_bits(x: int) -> int:
        cnt = 0
        while x > 0:
            cnt += x % 2
            x //= 2
        return cnt
        
    return list(map(nb_bits, range(n + 1)))
```

Time complexity: $O(n)$
The `while` loop will always run the same amount of time, depending on the system architecture (32/64 bits).

Space complexity: $O(n)$

### Dynamic programming approach

| n   | bits | count | Note      |
| --- | ---- | ----- | --------- |
| 0   | 0000 | 0     | base case |
|     |      |       |           |
| 1   | 0001 | 1     | 1 up + 1  |
|     |      |       |           |
| 2   | 0010 | 1     | 2 up + 1  |
| 3   | 0011 | 2     | 2 up + 1  |
|     |      |       |           |
| 4   | 0100 | 1     | 4 up + 1  |
| 5   | 0101 | 2     | 4 up + 1  |
| 6   | 0110 | 2     | 4 up + 1  |
| 7   | 0111 | 3     | 4 up + 1  |
|     |      |       |           |
| 8   | 1000 | 1     | 8 up + 1  |
| 9   | 1001 | 2     | 8 up + 1  |
| 10  | 1010 | 2     | 8 up + 1  |
| 11  | 1011 | 3     | 8 up + 1  |
| 12  | 1100 | 2     | 8 up + 1  |
| 13  | 1101 | 3     | 8 up + 1  |
| 14  | 1110 | 3     | 8 up + 1  |
| 15  | 1111 | 4     | 8 up + 1  |

```python
def count_bits(n: int) -> List[int]:
    # base case
    if n == 0:
        return [0]
        
    ans = [0]
    offset = 1
    for i in range(1, n + 1):
        if i == offset * 2:
            offset *= 2
        ans.append(1 + ans[i - offset])
        
    return ans
```

Time complexity: $O(n)$
Space complexity: $O(n)$
