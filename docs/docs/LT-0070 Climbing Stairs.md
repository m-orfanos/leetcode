---
tags:
- difficulty/easy
- topics/math
- topics/dynamic-programming
- topics/memoization
---

# 0070 Climbing Stairs

<https://leetcode.com/problems/climbing-stairs>

## Description

- Problem statement
    - You are climbing a staircase. It takes n steps to reach the top.
    - Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
- Constraints
    - $1 <= n <= 45$
- Examples
    - Example 1
        - Input: `n = 2`
        - Output: `2`
    - Example 2
        - Input: `n = 3`
        - Output: `3`

## Solutions

### Fibonacci sequence appears

Looking for a pattern…

```text
n = 1
1

n = 2
11
2

n = 3
111
12
21

n = 4
1111
112
121
211

n = 5
11111
1112
1121
1211
2111

...
```

| n   | cnt |
| --- | --- |
| 1   | 1   |
| 2   | 2   |
| 3   | 3   |
| 4   | 5   |
| 5   | 8   |
| 6   | 13  |

This is the Fibonacci sequence.

```typescript
function climb_stairs(n: number): number {
    let a = 0;
    let b = 1;
    while (n > 0) {
        const t = b;
        b += a;
        a = t;
        n -= 1;
    }
    return b;
}
```

Time complexity: $O(n)$
Space complexity: $O(1)$

### Combinatorics

Looking for an alternative solution using combinatorics…

```text
n = 1
1

n = 2
11
2

n = 3
111
12
21

n = 4
1111
112
121
211
22

n = 5
11111
1112
1121
1211
2111
122
212
221

...
```

grouping by step count

| n   | nb 1 steps | nb 2 steps | cnt |
| --- | ---------- | ---------- | --- |
| 1   | 1          | 0          | 1   |
|     |            | total      | 1   |

| n   | nb 1 steps | nb 2 steps | cnt |
| --- | ---------- | ---------- | --- |
| 2   | 2          | 0          | 1   |
|     | 0          | 1          | 1   |
|     |            | total      | 2   |

| n   | nb 1 steps | nb 2 steps | cnt |
| --- | ---------- | ---------- | --- |
| 3   | 3          | 0          | 1   |
|     | 1          | 1          | 2   |
|     |            | total      | 3   |

| n   | nb 1 steps | nb 2 steps | cnt |
| --- | ---------- | ---------- | --- |
| 4   | 4          | 0          | 1   |
|     | 2          | 1          | 3   |
|     | 0          | 2          | 1   |
|     |            | total      | 5   |

| n   | nb 1 steps | nb 2 steps | cnt |
| --- | ---------- | ---------- | --- |
| 5   | 5          | 0          | 1   |
|     | 3          | 1          | 4   |
|     | 1          | 2          | 3   |
|     |            | total      | 5   |

```text
take n = 5
there are 3 cases
    5 things to arrange    5!/(5!0!) = 1
    1 unique (5x1)
    
    4 things to arrange    4!/(3!1!) = 4
    2 unique (3x1, 1x2)
    
    3 things to arrange    3!/(1!2!) = 3
    2 unique (1x1, 2x2)
    
    1 + 4 + 3 = 8 total
```

others rest are similar

code

```typescript
function climb_stairs(n: number): number {
    const factorial = function fact() {
        const mem: { [key: number]: number } = {};
        return (n: number) => {
            if (n <= 1) {
                return 1;
            }
            
            if (mem[n] != null) {
                return mem[n];
            }
            
            mem[n] = n * factorial(n - 1);
            return mem[n];
        }
    }();
    
    let total = 0;
    let cnt1 = n;
    let cnt2 = 0;
    while (cnt1 >= 0 && cnt2 >= 0) {
        const top = factorial(cnt1 + cnt2);
        const bottom = factorial(cnt1) * factorial(cnt2);
        total += top / bottom;
        
        cnt1 -= 2;
        cnt2 += 1;
    }
    
    return total;
}
```

Time complexity: $O(n)$
While the factorial is $O(n)$ it is memoized; meaning it runs a single time on the first call and all subsequent calls are cached.

Space complexity: $O(n)$
