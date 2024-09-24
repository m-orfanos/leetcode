---
tags:
- difficulty/easy
---

# 0252 Meeting Rooms

<https://leetcode.com/problems/meeting-rooms>

## Description

This problem is locked behind a paywall. I copied the description from <https://leetcode.ca/all/252.html>.

- Problem statement
    - Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],…] (si < ei)`, determine if a person could attend all meetings.
- Constraints
    - $0 <= intervals.length <= 10^4$
    - $intervals[i].length == 2$
    - $0 <= starti < endi <= 10^6$
- Examples
    - Example 1
        - Input: `[[0,30],[5,10],[15,20]]`
        - Output: `false`
    - Example 2
        - Input: `[[7,10],[2,4]]`
        - Output: `true`

## Solutions

### Sort by start time and compare adjacent

sort meetings by their first element
iterate over array, compare end date of current with start date of next
if end date > start end, return false
else true

```text
[[0,30], [5,10], [15,20]]
     |----| compare these two
```

```typescript
function can_attend(meetings: number[][]): boolean {
    meetings.sort((a, b) => a[0] - b[0]);
    for (let i = 0; i < meetings.length - 1; i += 1) {
        const [, ei] = meetings[i];
        const [sj,] = meetings[i + 1];
        if (ei > sj) {
            return false;
        }
    }
    return true;
}
```

Time complexity: $O(n*log(n))$
Space complexity: $O(n)$
