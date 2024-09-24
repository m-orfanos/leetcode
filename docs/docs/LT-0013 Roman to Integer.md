---
tags:
- difficulty/easy
- topics/hash-table
- topics/math
- topics/string
---

# 0013 Roman to Integer

<https://leetcode.com/problems/roman-to-integer>

## Description

- Problem statement
    - Roman numerals are represented by seven different symbols
        - Symbol       Value
        - I             1
        - V             5
        - X             10
        - L             50
        - C             100
        - D             500
        - M             1000
        - For example,
            - `2` is written as `II` in Roman numeral, just two ones added together.
            - `12` is written as `XII`, which is simply `X + II`.
            - The number `27` is written as `XXVII`, which is `XX + V + II`.
        - Roman numerals are usually written largest to smallest from left to right.
        - However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four.
        - The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
            - `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
            - `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
            - `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.
    - Given a roman numeral, convert it to an integer.
- Constraints
    - $1 <= s.length <= 15$
    - `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
    - It is guaranteed that `s` is a valid roman numeral in the range `[1, 3999]`.
- Examples
    - Example 1
        - Input: `s = "III"`
        - Output: `3`
    - Example 2
        - Input: `s = "LVIII"`
        - Output: `58`
    - Example 3
        - Input: `s = "MCMXCIV"`
        - Output: `1994`

## Solutions

### Straightforward single-pass approach

parse the input string character by character
convert and add
look 1 ahead, if match `(IV, IX, XL, XC, CD, CM)`
adjust (subtract) amount by `(2,2,20,20,200,200)`

```typescript
function roman_to_integer(s: string): number {
    const symbols: { [key: string]: number } = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    };
    
    const adjust: { [key: string]: number } = {
        "IV": 2,
        "IX": 2,
        "XL": 20,
        "XC": 20,
        "CD": 200,
        "CM": 200,
    };
    
    let ans = 0;
    for (let i = 0; i < s.length; i += 1) {
        const si = s[i];
        const sj = s[i + 1];
        ans += symbols[si] - (adjust[si + sj] || 0);
    }
    
    return ans;
}
```

Time complexity: $O(n)$
Space complexity: $O(1)$
