---
tags:
- difficulty/easy
- topics/divide-and-conquer
- topics/bit-manipulation
---

# 0191 Number of 1 Bits

<https://leetcode.com/problems/number-of-1-bits>

## Description

- Problem statement
    - Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).
    - A set bit refers to a bit in the binary representation of a number that has a value of 1.
- Constraints
    - $1 <= n <= 2^{31} - 1$
- Examples
    - Example 1
        - Input: `n = 11`
        - Output: `3`
    - Example 2
        - Input: `n = 128`
        - Output: `1`
    - Example 3
        - Input: `n = 2147483645`
        - Output: `30`
- Follow up
    - If this function is called many times, how would you optimise it?

## Solutions

### Single-pass iterative approach

```python
def hamming_weight0(n: int) -> int:
    cnt = 0
    while n > 0:
        cnt += n % 2
        n //= 2
    return cnt
```

Time complexity: $O(b)$
Space complexity: $O(b)$
where b is the number of bits

### Bit twiddling magic #review

Solution I found while looking at the wikipedia page + others solutions. I have no idea how it works.

<https://en.wikipedia.org/wiki/Hamming_weight>

```java
public int hammingWeight(int x) {
    x = (x & 0x55555555) + ((x >> 1)  & 0x55555555);
    x = (x & 0x33333333) + ((x >> 2)  & 0x33333333);
    x = (x & 0x0F0F0F0F) + ((x >> 4)  & 0x0F0F0F0F);
    x = (x & 0x00FF00FF) + ((x >> 8)  & 0x00FF00FF);
    x = (x & 0x0000FFFF) + ((x >> 16) & 0x0000FFFF);
    
    return x;
}
```
