---
tags:
- difficulty/easy
- topics/array
- topics/depth-first-search
- topics/breadth-first-search
- topics/matrix
---

# 0733 Flood Fill

<https://leetcode.com/problems/flood-fill>

## Description

- Problem statement
    - An image is represented by an `m x n` integer grid image where `image[i][j]` represents the pixel value of the image.
    - You are also given three integers `sr`, `sc`, and `color`. You should perform a flood fill on the image starting from the pixel `image[sr][sc]`.
    - To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same colour as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same colour), and so on. Replace the colour of all of the aforementioned pixels with `color`.
    - Return the modified image after performing the flood fill.
- Constraints
    - $m == image.length$
    - $n == image[i].length$
    - $1 <= m, n <= 50$
    - $0 <= `image[i][j]`, color < 2^{16}$
    - $0 <= sr < m$
    - $0 <= sc < n$
- Examples
    - Example 1
        - Input: `image = [[1,1,1],[1,1,0],[1,0,1]]`, `sr = 1`, `sc = 1`, `color = 2`
        - Output: `[[2,2,2],[2,2,0],[2,0,1]]`
    - Example 2
        - Input: `image = [[0,0,0],[0,0,0]]`, `sr = 0`, `sc = 0`, `color = 0`
        - Output: `[[0,0,0],[0,0,0]]`

## Solutions

### Traverse the image using DFS

follow the steps in the description

- traverse grid using DFS
- when visiting a cell
    - ignore if already matching `colour`
    - update colour if matching the original colour
    - when update, traverse to the connected nodes, check boundaries

<https://en.wikipedia.org/wiki/Flood_fill#Stack-based_recursive_implementation_(four-way)>

```python
def flood_fill(image: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    color_old = image[row][col]
    
    # depth-first graph traversal
    to_fill = [(row, col)]
    while len(to_fill) > 0:
        x, y = to_fill.pop()
        
        if image[x][y] != color_old or image[x][y] == color:
            continue
            
        image[x][y] = color
        
        # next valid pixel
        if x > 0:
            to_fill.append((x - 1, y))
        if x < len(image) - 1:
            to_fill.append((x + 1, y))
        if y > 0:
            to_fill.append((x, y - 1))
        if y < len(image[x]) - 1:
            to_fill.append((x, y + 1))
            
    return image
```

Time complexity: $O(n*m)$
Space complexity: $O(n*m)$
