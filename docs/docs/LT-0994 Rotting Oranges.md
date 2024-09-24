---
tags:
- difficulty/medium
- topics/array
- topics/breadth-first-search
- topics/matrix
---

# 0994 Rotting Oranges

<https://leetcode.com/problems/rotting-oranges>

## Description

- Problem statement
    - You are given an `m x n` `grid` where each cell can have one of three values:
        - `0` representing an empty cell,
        - `1` representing a fresh orange, or
        - `2` representing a rotten orange.
    - Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
    - Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.
- Constraints
    - $m == grid.length$
    - $n == grid[i].length$
    - $1 <= m$, $n <= 10$
    - $grid[i,j]$ is `0`, `1`, or `2`.
- Examples
    - Example 1
        - Input: $grid = [[2,1,1],[1,1,0],[0,1,1]]$
        - Output: $4$
    - Example 2
        - Input: $grid = [[2,1,1],[0,1,1],[1,0,1]]$
        - Output: $-1$
    - Example 3
        - Input: $grid = [ [0,2] ]$
        - Output: $0$

## Solutions

### Repeated DFS approach (sorta)

find all the fresh oranges
DFS each fresh orange
repeat if not done

```python
def oranges_rotting(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    
    # EMPTY = 0
    FRESH = 1
    ROTTN = 2
    
    has_rotted = False
    batch = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == FRESH:
                batch.append((i, j))
            if grid[i][j] == ROTTN:
                has_rotted = True
                
    mins = 0
    while has_rotted:
        # elapse 1 min, check for new rotten
        rottn = []
        fresh = []
        for x, y in batch:
            is_fresh = True
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    is_fresh = is_fresh and grid[x + dx][y + dy] != ROTTN
            if is_fresh:
                fresh.append((x, y))
            else:
                rottn.append((x, y))
                
        # update grid
        for x, y in rottn:
            grid[x][y] = ROTTN
            
        # update state for next iteration
        # update `mins` only if newly rotten, otherwise this iteration
        # would not have been required
        batch = fresh
        if len(rottn) > 0:
            has_rotted = True
            mins += 1
        else:
            has_rotted = False
            
    return mins if len(batch) == 0 else -1
```

Time complexity: $O(n*m)$
Space complexity: $O(n*m)$
