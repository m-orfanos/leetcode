---
tags:
- difficulty/medium
- topics/array
- topics/dynamic-programming
- topics/breadth-first-search
---

# 0322 Coin Change

<https://leetcode.com/problems/coin-change>

## Description

- Problem statement
    - You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.
    - Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.
    - You may assume that you have an infinite number of each kind of coin.
- Constraints
    - $1 <= coins.length <= 12$
    - $1 <= coins[i] <= 2^{31} - 1$
    - $0 <= amount <= 10^4$
- Examples
    - Example 1
        - Input: $coins = [1,2,5]$, $amount = 11$
        - Output: $3$
    - Example 2
        - Input: $coins = [2]$, $amount = 3$
        - Output: $-1$
    - Example 3
        - Input: $coins = [1]$, $amount = 0$
        - Output: $0$

## Solutions  #review

### Combinatorics approach

This solution is a combination builder. It basically creates a set of coins and tests against the amount. There are no "wasted" combinations created.

For example:

```text
given
    [419, 408, 186, 83] 6249

it generates the following
    14    0    2    0
    14    0    1    2
    14    0    0    4
    13    1    2    0
    13    1    1    2
    13    1    0    4
    13    0    4    0
    13    0    3    2
    13    0    2    5
    13    0    1    7
    13    0    0    9
    12    2    2    0
    etc...
```

code

```python
def coin_change(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0
        
    coins = sorted(coins)[::-1]
    
    n = [0] * len(coins)
    amt = 0
    for i in range(len(coins)):
        n[i] = (amount - amt) // coins[i]
        amt += n[i] * coins[i]
        
    MAX_VALUE = 2**31 - 1
    best = MAX_VALUE
    while True:
        found = False
        
        if amt == amount:
            found = True
            best = min(best, sum(n))
            
        needle = -1
        if found:
            for i in range(len(coins)):
                if n[i] > 0:
                    needle = i
                    break
        else:
            for i in range(1, len(coins)):
                if n[len(coins) - 1 - i] > 0:
                    needle = len(coins) - 1 - i
                    break
                    
        if needle < 0:
            break
            
        n[needle] -= 1
        amt = 0
        for i in range(needle + 1):
            amt += n[i] * coins[i]
        for i in range(needle + 1, len(coins)):
            n[i] = (amount - amt) // coins[i]
            amt += n[i] * coins[i]
            
    return best if best != MAX_VALUE else -1
```

Obviously it times out because it's horrendously slow :D

Time complexity: $O(n!)$
Space complexity: $O(1)$

### Tabular, recursive, dynamic programming approach

```python
def coin_change(coins: List[int], amount: int) -> int:
    MAX_VALUE = 2**31 - 1
    d = [MAX_VALUE] * (amount + 1)
    
    def go(ci: int, amt: int) -> int:
        """
        Params:
          ci : the current coin being used
          amt: the amount left to convert to coins
        """
        if ci >= len(coins) or amt <= 0:
            return 0 if amt == 0 else MAX_VALUE
            
        if d[amt] != MAX_VALUE:
            return d[amt]
            
        # can either use or ignore this coin
        t0 = go(ci + 1, amt)
        t1 = 1 + go(ci, amt - coins[ci])
        t = min(t1, t0)
        
        d[amt] = t
        return t
        
    ans = go(0, amount)
    return ans if ans != MAX_VALUE else -1
```

Time complexity: $O(len(coins)*amount)$
Space complexity: $O(amount)$

### Tabular, iterative, bottom-up dynamic programming approach

calculate the minimum amount of coins for amounts `[1..n]`

```python
def coin_change(coins: List[int], amount: int) -> int:
    coins.sort()
    MAX_VALUE = amount // coins[0] + 1
    d = [MAX_VALUE] * (amount + 1)
    d[0] = 0
    for amt in range(1, amount + 1):
        for c in coins:
            if amt - c < 0:
                break
            if d[amt - c] != MAX_VALUE:
                d[amt] = min(d[amt], 1 + d[amt - c])
    return d[-1] if d[-1] != MAX_VALUE else -1
```

Time complexity: $O(len(coins)*amount)$
Space complexity: $O(amount)$
