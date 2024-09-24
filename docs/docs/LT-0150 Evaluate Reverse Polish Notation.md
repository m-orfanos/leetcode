---
tags:
- difficulty/medium
- topics/array
- topics/math
- topics/stack
---

# 0150 Evaluate Reverse Polish Notation

<https://leetcode.com/problems/evaluate-reverse-polish-notation>

## Description

- Problem statement
    - You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation. <https://en.wikipedia.org/wiki/Reverse_Polish_notation>
    - Evaluate the expression. Return an integer that represents the value of the expression.
- Constraints
    - $1 <= tokens.length <= 10^4$
    - $tokens[i]$ is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range $[-200, 200]$.
- Examples
    - Example 1
        - Input: `tokens = ["2","1","+","3","*"]`
        - Output: `9`
    - Example 2
        - Input: `tokens = ["4","13","5","/","+"]`
        - Output: `6`
    - Example 3
        - Input: `tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]`
        - Output: `22`

## Solutions

### Simply stack-based approach

push any non-operator into the stack
when processing operator, pop the stack twice, eval and push the result into the stack

```python
def eval_rpn(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            # can avoid the second pop in favour
            # of mutating the entry directly but wtv
            r = stack.pop()
            l = stack.pop()
            if token == "+":
                stack.append(l + r)
            elif token == "-":
                stack.append(l - r)
            elif token == "*":
                stack.append(l * r)
            else:  # elif token == "/":
                stack.append(int(l / r))
                
    return stack.pop()
```

Time complexity: $O(n)$
Space complexity: $O(n)$
