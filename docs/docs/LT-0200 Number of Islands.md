---
tags:
- difficulty/medium
- topics/tree
- topics/depth-first-search
- topics/binary-search-tree
- topics/binary-tree
---

# 0200 Number of Islands

<https://leetcode.com/problems/number-of-islands>

## Description

- Problem statement
    - Given an $m*n$ 2D binary grid `grid` which represents a map of `'1's` (land) and `'0's` (water), return the number of islands.
    - An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
- Constraints
    - $m == grid.length$
    - $n == grid[i].length$
    - $1 <= m$, $n <= 300$
    - $grid[i,j]$ is $'0'$ or $'1'$.
- Examples
    - Example 1
        - Input: `grid =`
            - `[["1","1","1","1","0"],`
            - `["1","1","0","1","0"],`
            - `["1","1","0","0","0"],`
            - `["0","0","0","0","0"]]`
        - Output: `1`
    - Example 2
        - Input: `grid =`
            - `[["1","1","0","0","0"],`
            - `["1","1","0","0","0"],`
            - `["0","0","1","0","0"],`
            - `["0","0","0","1","1"]]`
        - Output: $3$

## Solutions

### Modified DFS approach

similar to [[LT-0733 Flood Fill]]

```python
def num_islands(grid: List[List[str]]) -> int:
    n = len(grid)
    m = len(grid[0])
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                s = [(i, j)]
                while s:
                    x, y = s.pop()
                    if grid[x][y] != "1":
                        continue
                    grid[x][y] = cnt
                    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        if 0 <= x + dx < n and 0 <= y + dy < m:
                            s.append((x + dx, y + dy))
                cnt += 1
                
    return cnt
```

Time complexity: $O(n*m)$
Space complexity: $O(n*m)$
