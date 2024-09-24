---
tags:
- difficulty/medium
- topics/stack
- topics/design
---

# 0155 Min Stack

<https://leetcode.com/problems/min-stack>

## Description

- Problem statement
    - Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    - Implement the MinStack class:
        - `MinStack()` initialises the stack object.
        - `void push(int val)` pushes the element val onto the stack.
        - `void pop()` removes the element on the top of the stack.
        - `int top()` gets the top element of the stack.
        - `int getMin()` retrieves the minimum element in the stack.
    - You must implement a solution with `O(1)` time complexity for each function.
- Constraints
    - $-2^{31} <= val <= 2^{31} - 1$
    - Methods `pop`, `top` and `getMin` operations will always be called on non-empty stacks.
    - At most $3*10^4$ calls will be made to `push`, `pop`, `top`, and `getMin`.

## Solutions

### Store the state every time

When pushing at the top of the stack, also push the current min.
Could also use two stacks.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if self.stack:
            min_val = self.stack[-1][1]
        else:
            min_val = val
        min_val = min(val, min_val)
        
        self.stack.append((val, min_val))
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
```
