---
tags:
- difficulty/easy
- topics/array
- topics/math
- topics/string
- topics/bit-manipulation
- topics/simulation
---

# 0067 Add Binary

<https://leetcode.com/problems/add-binary>

## Description

- Problem statement
    - Given two binary strings `a` and `b`, return their sum as a binary string.
- Constraints
    - $1 <= a.length, b.length <= 10^4$
    - `a` and `b` consist only of `'0'` or `'1'` characters.
    - Each string does not contain leading zeros except for the zero itself.
- Examples
    - Example 1
        - Input: `a = "11"`, `b = "1"`
        - Output: `"100"`
    - Example 2
        - Input: `a = "1010"`, `b = "1011"`
        - Output: `"10101"`

## Solutions

### Use standard library

```python
def add_binary(a: str, b: str) -> str:
    an = int(f"0b{a}", base=0)
    bn = int(f"0b{b}", base=0)
    cn = an + bn
    return bin(cn)[2:]
```

Time complexity: $O(max(a,b))$
Space complexity: $O(max(a,b))$

### Convert, add, and convert

roll your own "parseint" and "tostring" implementations

string base 2 -> integer base 10 -> add -> string base 2

```python
def add_binary(a: str, b: str) -> str:
    def to_int(s: str) -> int:
        base = 2
        ans = 0
        for ch in s:
            digit = 1 if ch == "1" else 0
            ans = ans * base + digit
        return ans
        
    def to_bin(n: int) -> str:
        if n == 0:
            return "0"
        base = 2
        digits = []
        while n > 0:
            digits.append("1" if n % base == 1 else "0")
            n //= base
        return "".join(digits[::-1])
        
    aa = to_int(a)
    bb = to_int(b)
    cc = aa + bb
    
    return to_bin(cc)
```

Time complexity: $O(max(a,b))$
Space complexity: $O(max(a,b))$

### Single-Pass Binary Arithmetic

Use addition as taught in grade school (don't forget to carry the ones!)

```typescript
function add_binary(a: string, b: string): string {
    const size = a.length > b.length ? a.length : b.length;
    const ans = [];
    let carry = 0;
    for (let i = 0; i < size; i += 1) {
        const m = (a[a.length - 1 - i] || "0") === "0" ? 0 : 1;
        const n = (b[b.length - 1 - i] || "0") === "0" ? 0 : 1;
        const curr = carry + m + n;
        // curr
        // 0 0b00
        // 1 0b01
        // 2 0b10
        // 3 0b11
        if (curr === 0) {
            ans.push("0");
            carry = 0;
        } else if (curr === 1) {
            ans.push("1");
            carry = 0;
        } else if (curr === 2) {
            ans.push("0");
            carry = 1;
        } else if (curr === 3) {
            ans.push("1");
            carry = 1;
        }
    }
    
    if (carry > 0) {
        ans.push("1");
    }
    
    return ans.reverse().join("");
}
```

Time complexity: $O(max(a,b))$
Space complexity: $O(max(a,b))$
