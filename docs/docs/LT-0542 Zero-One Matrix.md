---
tags:
- difficulty/medium
- topics/array
- topics/dynamic-programming
- topics/breadth-first-search
- topics/matrix
---

# 0542 Zero-One Matrix

<https://leetcode.com/problems/01-matrix>

## Description

- Problem statement
    - Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell.
    - The distance between two adjacent cells is `1`.
- Constraints
    - $m == mat.length$
    - $n == mat[i].length$
    - $1 <= m, n <= 10^4$
    - $1 <= m * n <= 10^4$
    - $mat[i,j]$ is either $0$ or $1$.
    - There is at least one $0$ in `mat`.
- Examples
    - Example 1
        - Input: $mat = [[0,0,0],[0,1,0],[0,0,0]]$
        - Output: $[[0,0,0],[0,1,0],[0,0,0]]$
    - Example 2
        - Input: $mat = [[0,0,0],[0,1,0],[1,1,1]]$
        - Output: $[[0,0,0],[0,1,0],[1,2,1]]$

## Solutions

### Brute force

```python
def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    ans = [[sys.maxsize] * len(mat[i]) for i in range(len(mat))]
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y] == 0:
                for i in range(len(mat)):
                    for j in range(len(mat[i])):
                        dist = abs(x - i) + abs(y - j)
                        ans[i][j] = min(ans[i][j], dist)
    return ans
```

Time complexity: $O(m^2*n^2)$
Space complexity: $O(m*n)$

### DFS approach

```python
def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    nrows = len(mat)
    ncols = len(mat[0])
    
    # store all the 0-valued cells into a queue
    # set all over values in the matrix to the max integer
    q = deque()
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y] == 0:
                q.append([x, y])
            else:
                mat[x][y] = sys.maxsize
                
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # perform a BFS across the matrix with 0-valued cells as entry points
    # important! cells may be visited multiple times
    while len(q) > 0:
        [x, y] = q.popleft()
        
        # visit neighbors around (x,y)
        for [dx, dy] in directions:
            xn = x + dx
            yn = y + dy
            if 0 <= xn < nrows and 0 <= yn < ncols and mat[xn][yn] > mat[x][y] + 1:
                # update the distance of this neighbor to a 0-valued cell
                # cells needs to be traversed again each time there's an update
                mat[xn][yn] = mat[x][y] + 1
                q.append([xn, yn])
                
    return mat
```

Time complexity: $O(m*n)$
Space complexity: $O(m*n)$
