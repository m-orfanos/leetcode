---
tags:
- difficulty/easy
- topics/stack
- topics/design
- topics/queue
---

# 0232 Implement Queue using Stacks

<https://leetcode.com/problems/implement-queue-using-stacks>

## Description

- Problem statement
    - Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).
    - Implement the `MyQueue` class:
        - `void push(int x)` Pushes element x to the back of the queue.
        - `int pop()` Removes the element from the front of the queue and returns it.
        - `int peek()` Returns the element at the front of the queue.
        - `boolean empty()` Returns true if the queue is empty, false otherwise.
    - Notes:
        - You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
        - Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
- Contraints
    - $1 <= x <= 9$
    - At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.
    - All the calls to `pop` and `peek` are valid.
- Examples
    - Example 1
        - Input
            - `["MyQueue", "push", "push", "peek", "pop", "empty"]`
            - `[[], [1], [2], [], [], []]`
        - Output
            - `[null, null, null, 1, 1, false]`
        - Explanation
            - `MyQueue myQueue = new MyQueue();`
            - `myQueue.push(1); // queue is: [1]`
            - `myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)`
            - `myQueue.peek(); // return 1`
            - `myQueue.pop(); // return 1, queue is [2]`
            - `myQueue.empty(); // return false`
- Follow-up
    - Can you implement the queue such that each operation is amortized `O(1)` time complexity?
    - In other words, performing `n` operations will take overall `O(n)` time even if one of those operations may take longer.

## Solutions

### Use two stacks

Goal: implement a queue data structure, backed by two stacks

assuming a stack is backed by an array/list

- stack
    - push/pop/peek operations are all against the "top of the stack" (e.g. end of the array)
    - size is the length of the array

```text
[1, 2, 3, 4]
          | "top of stack"
          |->push/pop/peek
```

assuming a queue is backed by an array/list

- queue
    - queue (push): insert at the front of the array
    - dequeue (pop): remove from the end of the array
    - peek: view from the end of the array

```text
[1, 2, 3, 4]
 |        |
 |->queue |
          |->dequeue/peek
```

assuming a queue is backed by two stacks

```text
    stack 1         stack 2
    [1, 2, 3, 4]    []
    
dequeue
    [1, 2, 3, 4]    []
              |-> pop
    steps
        move all elements to stack 1
        pop stack 1
        
enqueue
    [1, 2, 3, 4]    []
    []              [4, 3, 2, 1]
                              |-> push
    steps
        move all elements to stack 2
        push stack 2
        
peek
    similar to dequeue
    steps
        move all elements to stack 1
        peek stack 1
        
size
    size stack 1 + size stack 2
```

The number of operations on the stacks should be minimised (i.e. avoid moving elements). The above already takes that into account.

shown as code

```typescript
class MyQueue {
    
    first: number[];
    second: number[];
    
    constructor() {
        this.first = [];
        this.second = [];
    }
    
    push(x: number): void {
        this.move_to_first();
        this.first.push(x);
    }
    
    pop(): number {
        this.move_to_second();
        return this.second.pop()!;
    }
    
    peek(): number {
        this.move_to_second();
        return this.second[this.second.length - 1];
    }
    
    empty(): boolean {
        return this.first.length === 0 && this.second.length === 0;
    }
    
    private move_to_first() {
        while (this.second.length > 0) {
            this.first.push(this.second.pop()!);
        }
    }
    
    private move_to_second() {
        while (this.first.length > 0) {
            this.second.push(this.first.pop()!);
        }
    }
}
```
