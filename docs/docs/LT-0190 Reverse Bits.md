---
tags:
- difficulty/easy
- topics/array
- topics/divide-and-conquer
- topics/bit-manipulation
---

# 0190 Reverse Bits

<https://leetcode.com/problems/reverse-bits>

## Description

- Problem statement
    - Reverse bits of a given 32 bits unsigned integer.
- Notes
    - In some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
    - In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer `-3` and the output represents the signed integer `-1073741825`.
- Constraints
    - The input must be a binary string of length 32
- Examples
    - Example 1
        - Input: `n = 00000010100101000001111010011100`
        - Output: `964176192 (00111001011110000010100101000000)`
    - Example 2
        - Input: `n = 11111111111111111111111111111101`
        - Output: `3221225471 (10111111111111111111111111111111)`
- Follow up
    - If this function is called many times, how would you optimise it?

## Solutions

### Bits and bits and bits

```python
def reverse_bits(n: int) -> int:
    rev = 0
    for _ in range(32):
        rev = 2 * rev + n % 2
        n //= 2
    return rev
```

Time complexity: $O(1)$ (it's constant…, right?)
Space complexity: $O(1)$

### Bit twiddling magic #review

Solution copied from LeetCode, I have no idea how it works.

```java
public int reverseBits(int num) {
    num = ((num & 0xffff0000) >>> 16) | ((num & 0x0000ffff) << 16);
    num = ((num & 0xff00ff00) >>> 8) | ((num & 0x00ff00ff) << 8);
    num = ((num & 0xf0f0f0f0) >>> 4) | ((num & 0x0f0f0f0f) << 4);
    num = ((num & 0xcccccccc) >>> 2) | ((num & 0x33333333) << 2);
    num = ((num & 0xaaaaaaaa) >>> 1) | ((num & 0x55555555) << 1);
    
    return num;
}
```

Time complexity: $O(1)$
Space complexity: $O(1)$
