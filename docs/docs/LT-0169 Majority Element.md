---
tags:
- difficulty/easy
- topics/array
- topics/hash-table
- topics/divide-and-conquer
- topics/sorting
- topics/counting
---

# 0169 Majority Element

<https://leetcode.com/problems/majority-element>

## Description

- Problem description
    - Given an array `nums` of size `n`, return the majority element.
    - The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.
- Constraints
    - $n == nums.length$
    - $1 <= n <= 5 * 10^4$
    - $-10^9 <= nums[i] <= 10^9$
- Examples
    - Example 1
        - Input: `nums = [3,2,3]`
        - Output: `3`
    - Example 2
        - Input: `nums = [2,2,1,1,1,2,2]`
        - Output: `2`
- Follow-up
    - Could you solve the problem in linear time and in `O(1)` space?

## Solutions

### Simple counting with histogram

```python
def majority_element(nums: List[int]) -> int:
    counter = {}
    for n in nums:
        cnt = 1 + counter.get(n, 0)
        if cnt > len(nums) // 2:
            return n
        counter[n] = cnt
    return -1
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Boyer Moore (single) majority-vote algorithm

- picture a "bag" that can hold elements
- traverse the array, when visit element
    - if the bag it empty, add the element to it (can be a counter)
    - else, remove an element from the bag (decrement counter)
    - repeat
- the remaining element in the bag is the majority element

| i   | n   | bag   |
| --- | --- | ----- |
| 0   | 2   | (2)   |
| 1   | 2   | (2,2) |
| 2   | 1   | (2)   |
| 3   | 1   | ()    |
| 4   | 1   | (1)   |
| 5   | 2   | ()    |
| 6   | 2   | (2)   |

Instead of an array/list, the bag can be two variables `(cnt, majority)` or a map with a single entry `{majority: cnt}`.

```typescript
function majority_element(nums: number[]): number {
    let cnt = 1;
    let majority = nums[0];
    for (const n of nums) {
        cnt += majority === n ? 1 : -1;
        if (cnt === 0) {
            cnt = 1;
            majority = n;
        }
    }
    return majority;
}
```

Time complexity: $O(n)$
Space complexity: $O(1)$

#### Addendum: Boyer Moore (multi) majority-vote algorithm

The above can be extended to returning the n-majority:

- use `n` number of bags instead of `1` (use a map)
- traverse the array, when visiting an element:
    - if ONE of the bags is empty, add the element to it
    - else, remove an element from EVERY bag
    - repeat
- the remaining elements in the bags are the majority element (including their count)
