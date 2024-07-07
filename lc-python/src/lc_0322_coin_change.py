import unittest
from typing import List


def coin_change0(coins: List[int], amount: int) -> int:
    """
    This solution is a combination builder. It basically
    creates a set of coins and tests against the amount.
    There are no "wasted" combinations created.

    For example, it generates the following when

    given [419, 408, 186, 83] 6249

    14	0	2	0
    14	0	1	2
    14	0	0	4
    13	1	2	0
    13	1	1	2
    13	1	0	4
    13	0	4	0
    13	0	3	2
    13	0	2	5
    13	0	1	7
    13	0	0	9
    12	2	2	0
    etc...

    Obviously it times out because it's horrendously slow :D

    Time complexity: O(n!)
    Space complexity: O(1)
    """
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


def coin_change1(coins: List[int], amount: int) -> int:
    """
    Tabular, recursive, dynamic programming approach.

    Time complexity: O(len(coins)*amount)
    Space complexity: O(amount)
    """
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


def coin_change2(coins: List[int], amount: int) -> int:
    """
    Tabular, iterative, bottom-up dynamic programming approach.

    Time complexity: O(len(coins)*amount)
    Space complexity: O(amount)
    """
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


class TestCoinChange(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[1, 2, 5], 11, 3],
            [[2], 3, -1],
            [[1], 0, 0],
            [[1, 2147483647], 2, 2],
            [[1, 2, 5], 100, 20],
            [[186, 419, 83, 408], 6249, 20],
            [[3, 7, 405, 436], 8839, 25],
            [[411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422], 9864, 24],
        ]
        return data

    def test_coin_change0(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            # this approach is too slow for some test cases
            if i > 6:
                continue

            a = tc[0]
            b = tc[1]
            expected = tc[2]

            actual = coin_change0(a, b)

            self.assertEqual(actual, expected, f"coin_change0 test case {i} failed")

    def test_coin_change1(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            # the stack blows up for some test cases
            if i > 5:
                continue

            a = tc[0]
            b = tc[1]
            expected = tc[2]

            actual = coin_change1(a, b)

            self.assertEqual(actual, expected, f"coin_change1 test case {i} failed")

    def test_coin_change2(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = tc[0]
            b = tc[1]
            expected = tc[2]

            actual = coin_change2(a, b)

            self.assertEqual(actual, expected, f"coin_change2 test case {i} failed")


if __name__ == "__main__":
    unittest.main()
