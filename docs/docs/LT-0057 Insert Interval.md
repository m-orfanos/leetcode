---
tags:
- difficulty/medium
- topics/array
---

# 0057 Insert Interval

<https://leetcode.com/problems/insert-interval>

## Description

- Problem statement
    - You are given an array of non-overlapping `intervals` intervals where `intervals[i] = [starti, endi]` represent the start and the end of the `ith` interval and `intervals` is sorted in ascending order by `starti`.
    - You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.
    - Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).
    - Return `intervals` after the insertion.
    - Note that you don't need to modify `intervals` in-place. You can make a new array and return it.
- Constraints
    - $0 <= intervals.length <= 10^4$
    - $intervals[i].length == 2$
    - $0 <= starti <= endi <= 10^5$
    - `intervals` is sorted by `starti` in ascending order.
    - $newInterval.length == 2$
    - $0 <= start <= end <= 10^5$
- Examples
    - Example 1
        - Input: `intervals = [[1,3],[6,9]]`, `newInterval = [2,5]`
        - Output: `[[1,5],[6,9]]`
    - Example 2
        - Input: `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]`, `newInterval = [4,8]`
        - Output: `[[1,2],[3,10],[12,16]]`

## Solutions

### Append, sort and merge

```python
def insert0(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # add `newInterval` to the list and sort
    intervals.append(newInterval)
    intervals.sort(key=lambda x: x[0])
    
    # create a new list to hold the response
    # either append OR merge the ith element into the response
    ans = [intervals[0]]
    for [si, ei] in intervals[1:]:
        [sp, ep] = ans[-1]
        if sp <= si <= ep or sp <= ei <= ep:
            st = min(sp, si)
            et = max(ep, ei)
            ans[-1] = [st, et]
        else:
            ans.append([si, ei])
            
    return ans
```

Time complexity: $O(n*log(n))$
Space complexity: $O(n)$
\

### Add and merge

```python
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    ans = []
    
    # add intervals until overlap occurs
    i = 0
    while i < len(intervals):
        [si, ei] = intervals[i]
        if ei >= newInterval[0]:
            break
        ans.append([si, ei])
        i += 1
        
    # merge overlapping intervals
    merged = newInterval
    while i < len(intervals):
        [si, ei] = intervals[i]
        [sm, em] = merged
        if si > em:
            break
        merged = [min(sm, si), max(em, ei)]
        i += 1
        
    # add merged interval
    ans.append(merged)
    
    # add remaining intervals
    for interval in intervals[i:]:
        ans.append(interval)
        
    return ans
```

Time complexity: $O(n)$
Space complexity: $O(n)$
