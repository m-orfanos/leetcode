---
tags:
- difficulty/medium
- topics/array
- topics/math
- topics/divide-and-conquer
- topics/geometry
- topics/sorting
- topics/heap
- topics/quick-select
---

# 0973 K Closest Points to Origin

<https://leetcode.com/problems/k-closest-points-to-origin>

## Description

- Problem statement
    - Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.
    - The distance between two points on the X-Y plane is the Euclidean distance (i.e., $\sqrt{(x1 - x2)^2 + (y1 - y2)^2}$.
    - You may return the answer in any order.
    - The answer is guaranteed to be unique (except for the order that it is in).
- Constraints
    - $1 <= k <= points.length <= 10^4$
    - $-10^4 <= xi, yi <= 10^4$
- Examples
    - Example 1
        - Input: $points = [[1,3],[-2,2]]$, $k = 1$
        - Output: $[ [-2,2] ]$
    - Example 2
        - Input: $points = [[3,3],[5,-1],[-2,4]]$, $k = 2$
        - Output: $[[3,3],[-2,4]]$

## Solutions

### Brute-force approach (kinda)

```python
def k_closest0(points: List[List[int]], k: int) -> List[List[int]]:
    def compare(a: List[int], b: List[int]) -> int:
        return a[0] * a[0] + a[1] * a[1] - b[0] * b[0] - b[1] * b[1]
        
    points.sort(key=cmp_to_key(compare))
    
    return points[:k]
```

Time complexity: $O(n*log(n))$
Space complexity: $O(n)$

### Max-heap approach

```python
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    q = []
    for i in range(k):
        [x, y] = points[i]
        heappush(q, [-(x * x + y * y), [x, y]])
        
    for [x, y] in points[k:]:
        heappushpop(q, [-(x * x + y * y), [x, y]])
        
    return [heappop(q)[1] for _ in range(k)]
```

Time complexity: $O(n*log(k))$
Space complexity: $O(k)$
`headpush`, `heappop`, `heappushpop` are all $O(log(k))$, where `k` is the number of elements in the heap

### Modified quick-sort #review

A modified quick-sort approach (aka `quickselect`) shared by another LeetCode user.

<https://en.wikipedia.org/wiki/Quicksort>
<https://en.wikipedia.org/wiki/Quickselect>

```python
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    def mid(low: int, high: int) -> int:
        return high - (high - low) // 2
        
    def euclid(p: List[int]) -> int:
        return p[0] * p[0] + p[1] * p[1]
        
    def swap(a: int, b: int):
        tmp = points[a]
        points[a] = points[b]
        points[b] = tmp
        
    # alternative to `hoare_partition`
    # def lomuto_partition(lo: int, hi: int) -> int:
    #     pivot = points[mid(lo, hi)]
    #
    #     i = lo
    #     for j in range(lo, hi):
    #         if euclid(points[j]) - euclid(pivot) < 0:
    #             swap(i, j)
    #             i += 1
    #
    #     swap(i, hi)
    #
    #     return i
    
    def hoare_partition(lo: int, hi) -> int:
        pivot = points[mid(lo, hi)]
        
        l = lo
        r = hi
        while True:
            while euclid(points[l]) - euclid(pivot) < 0:
                l += 1
            while euclid(points[r]) - euclid(pivot) > 0:
                r -= 1
            if l >= r:
                break
            swap(l, r)
            
        return r
        
    partition = hoare_partition
    
    l = 0
    r = len(points) - 1
    while l <= r:
        p = partition(l, r)
        if p == k:
            break
        elif p < k:
            l = p + 1
        else:
            r = p - 1
            
    return points[:k]
```

Time complexity: $O(n)$ (average), $O(n^2)$ (worst)
Space complexity: $O(1)$
