---
tags:
- difficulty/medium
- topics/array
- topics/two-pointers
- topics/sorting
---

# 0015 Three Sum

<https://leetcode.com/problems/3sum>

## Description

- Problem statement
    - Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
    - Notice that the solution set must not contain duplicate triplets.
- Constraints
    - $3 <= nums.length <= 3000$
    - $-10^5 <= nums[i] <= 10^5$
- Examples
    - Example 1
        - Input: $nums = [-1,0,1,2,-1,-4]$
        - Output: $[[-1,-1,2],[-1,0,1]]$
    - Example 2
        - Input: $nums = [0,1,1]$
        - Output: $[]$
    - Example 3
        - Input: $nums = [0,0,0]$
        - Output: $[ [0,0,0] ]$

## Solutions

This problem is a more complicated version of [[LT-0001 Two Sum]].

### Brute-force approach (kinda)

iterate over all index pairs `(i,j)`
find index `c` in map such that `l[i] + l[j] + l[k] = 0`

some care is taken to avoid duplicate values (and by extension using a set)

- the input list is sorted in order to iterate over `i=[0,n)` and `j=[i+1,n)`
- consecutive values of `l[i]` and `l[j]` are duplicated, so skipped
- when retrieving elements from the map, make sure indices are greater than `i` and `j`

```python
def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    
    # map of values to indices
    # {v1:[i1,j1,k1,...], v2:[i2,j2,k2,...]}
    d = {}
    for i in range(len(nums)):
        ni = nums[i]
        if ni not in d:
            d[ni] = []
        d[ni].append(i)
        
    triplets = []
    ni = None
    nj = None
    for i in range(len(nums)):
        if ni == nums[i]:
            # skip duplicates
            continue
        ni = nums[i]
        for j in range(i + 1, len(nums)):
            if nj == nums[j]:
                # skip duplicates
                continue
            nj = nums[j]
            t = -1 * (ni + nj)
            if t in d:
                for k in d[t]:
                    # skip duplicates
                    if i < j < k:
                        nk = nums[k]
                        triplets.append([ni, nj, nk])
                        break
                        
    return triplets
```

Time complexity: $O(n^3)$
Space complexity: $O(n)$

### Two pointer approach

sort the input array

```text
i    <----------------->
        <----------->
           <----->
-4, -2, 0, 1, 2, 3, 4, 6
```

the first triplet is `(-4,-2,6)`

the next triplet, if it exists _must_ be contained within the range `[j,k]`. This is because `l[j+1] >= l[j]` and `l[k-1] <= l[k]`. This allows us to iterate over an increasingly shrinking range/window (i.e. "two pointers").

finally, add some code to avoid duplicates

```python
def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    
    n = len(nums) - 1
    prev = None
    
    triplets = []
    for i in range(len(nums)):
        # skip duplicates
        if nums[i] == prev:
            continue
            
        prev = nums[i]
        target = 0 - nums[i]
        
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                triplets.append((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
                
                # skip duplicates
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
                    
    return triplets
```

Time complexity: $O(n^2)$
Space complexity: $O(n)$

### Divide-and-conquer approach #review

Split input list into 3 parts: positives, negatives, zeroes.
For zeroes, search for `-n` and `n`.
For non-zeroes, the sum `a+b+c=0` requires either 2 positives or negatives; we can calculate `a+b` and search `c` in the remaining partition.

```python
def three_sum(nums: List[int]) -> List[List[int]]:
    # split nums into 3 partitions
    positives = {}
    negatives = {}
    zeroes = 0
    for n in nums:
        if n > 0:
            if n not in positives:
                positives[n] = 0
            positives[n] += 1
        elif n < 0:
            if n not in negatives:
                negatives[n] = 0
            negatives[n] += 1
        else:
            zeroes += 1
            
    triples = []
    
    # case (0,n,-n), e.g. 1 positive + 1 negative
    # case (0,-n,n), ignored, it's the mirror of above
    if zeroes > 0:
        for n in positives.keys():
            if -n in negatives:
                triples.append([0, n, -n])
        if zeroes > 2:
            triples.append([0, 0, 0])
            
    # case (p1,p2,n), e.g. 2 positives + 1 negative
    # case (n1,n2,p), e.g. 2 negatives + 1 positive
    for xs, ys in ((positives, negatives), (negatives, positives)):
        for n1 in xs.keys():
            for n2 in xs.keys():
                # skips duplicate/invalid entries
                if n1 > n2 or (n1 == n2 and xs[n1] < 2):
                    continue
                if -(n1 + n2) in ys:
                    triples.append([n1, n2, -(n1 + n2)])
                    
    return triples
```

Time complexity: $O(n^2)$
Space complexity: $O(n)$
