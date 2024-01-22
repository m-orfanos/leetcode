from typing import List

from lib import max_subarray


def max_profit(prices: List[int]) -> int:
    """
    Traverse the array a single time while keeping track of the
        1) maximum profit up until the "current" day/index
        2) minimum buy price

    When a smaller buy price is found, update the buy price to this value.

    This is correct because the maximum profit from the previous days has already
    been calculated AND the smaller buy price is now the hypothetical floor to the
    next price points.

    Time complexity: O(n)
    Space complexity: O(1)

    This solution is essentially a condensed version of the approach described
    below using Kadane's algorithm.
    """
    profit = 0
    buy = prices[0]
    for sell in prices[1:]:
        profit = max(profit, sell - buy)
        buy = min(buy, sell)
    return profit


def max_profit0(prices: List[int]) -> int:
    """
    Brute force approach. This solution times out.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = max(profit, prices[j] - prices[i])
    return profit


def max_profit1(prices: List[int]) -> int:
    """
    Given [7, 1, 5, 3, 6, 4]

    1) Calculate the difference between neighbouring elements

        1 - 7 = -6
        5 - 1 = +4
        3 - 5 = -2
        6 - 3 = +3
        4 - 6 = -2

        [-6, +4, -2, +3, -2]

    This approach is easier to understand if the initial array is visualized as
    a graph with coordiates (0,7), (1,1), etc.

    Find the two points (xn,yn) and (xm,ym) that maximizes ym - yn with xn < xm.
    This can be done by adding the immediate differences (y2-y1) + (y3-y2) + etc.

    The answer is the largest sum of any contiguous segment, e.g. Kadane's algorithm.

    Time complexity: O(n)
    Space complexity: O(n)

    This approach can be further improved by dropping the intermediate array, giving a
    space complexity of O(1), but was not done here for the sack of clarity.
    """
    xs = []
    for i in range(1, len(prices)):
        xs.append(prices[i] - prices[i - 1])
    return max(0, max_subarray(xs))
