import unittest
from typing import List

from src.shared.lib import max_subarray


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


def max_profit(prices: List[int]) -> int:
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
    a graph with coordinates (0,7), (1,1), etc.

    Find the two points (xn,yn) and (xm,ym) that maximizes ym - yn with xn < xm.
    This can be done by adding the immediate differences (y2-y1) + (y3-y2) + etc.

    The answer is the largest sum of any contiguous segment, e.g. Kadane's algorithm.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    xs = []
    for i in range(1, len(prices)):
        xs.append(prices[i] - prices[i - 1])
    return max(0, max_subarray(xs))


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[7, 1, 5, 3, 6, 4], 5],
            [[7, 6, 4, 3, 1], 0]
        ]
        return data

    def test_best_time_to_buy_and_sell_stock(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            actual = max_profit(tc[0])
            expected = tc[1]
            self.assertEqual(actual, expected, f"{i} {tc[0]}")

    def test_best_time_to_buy_and_sell_stock0(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            actual = max_profit0(tc[0])
            expected = tc[1]
            self.assertEqual(actual, expected, f"{i} {tc[0]}")


if __name__ == "__main__":
    unittest.main()