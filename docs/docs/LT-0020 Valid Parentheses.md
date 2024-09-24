---
tags:
- difficulty/easy
- topics/string
- topics/stack
---

# 0020 Valid Parentheses

<https://leetcode.com/problems/valid-parentheses>

## Description

- Problem statement
    - Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
    - An input string is valid if:
        - Open brackets must be closed by the same type of brackets.
        - Open brackets must be closed in the correct order.
        - Every close bracket has a corresponding open bracket of the same type.
- Constraints
    - $1 <= s.length <= 10^4$
    - `s` consists of parentheses only `'()[]{}'`.
- Examples
    - Example 1
        - Input: `s = "()"`
        - Output: `true`
    - Example 2
        - Input: `s = "()[]{}"`
        - Output: `true`
    - Example 3
        - Input: `s = "(]"`
        - Output: `false`

## Solutions

### Solution 1: Stack-based approach

- Steps
    - Read the string character by character
    - Put "open brackets" `({[` into a stack
    - When a "close bracket" `)}]` is found, pop the stack and check if matching pair

Example 1: input `()[]{}`

| iteration | character | stack | check   |
| --------- | --------- | ----- | ------- |
| 0         | `(`       | empty | n/a     |
| 1         | `)`       | `(`   | `()` ✅ |
| 2         | `[`       | empty | n/a     |
| 3         | `]`       | `[`   | `[]` ✅ |
| …         | …         | …     | …       |

Example 2: input `(([]))`

| iteration | character | stack | check   |
| --------- | --------- | ----- | ------- |
| 0         | `(`       | empty | n/a     |
| 1         | `(`       | `(`   | n/a     |
| 2         | `[`       | `((`  | n/a     |
| 3         | `]`       | `(([` | `[]` ✅ |
| 4         | `)`       | `((`  | `()` ✅ |
| 5         | `)`       | `(`   | `()` ✅ |

- Edge cases
    - input string begins with a "close bracket"
        - example `)()[]`
        - solution: check if stack is empty before pop step
    - input string is 1 character (or odd length)
        - example `(`, `()(`
        - add a guard, check length is even
    - input string has more "open brackets" than "close brackets"
        - example `((((`
        - when iteration is done, check if stack is empty

```python
def is_valid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False
        
    tokens = {"(": ")", "{": "}", "[": "]"}
    stack = []
        
    for ch in s:
        if ch in "({[":
            # opening bracket
            stack.append(ch)
        else:
            # closing bracket
            if len(stack) == 0:
                # no brackets to match
                return False
                
            # try-match brackets
            b = stack.pop()
            if tokens[b] != ch:
                return False
                
    return len(stack) == 0
```

Time complexity: $O(n)$
Space complexity: $O(n)$
