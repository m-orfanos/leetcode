from typing import List, Tuple
import unittest

from lib import read_lines, chunks, to_list_int
from lc_0121_best_time_to_buy_and_sell_stock import max_profit, max_profit0, max_profit1


def parse_input() -> List[Tuple[List[int], int]]:
    lines = read_lines("lc_0121_best_time_to_buy_and_sell_stock.dat")
    lines_chunks = chunks(lines, 2)
    ans = []
    for chunk in lines_chunks:
        l = to_list_int(chunk[0])
        n = int(chunk[1])
        ans.append((l, n))
    return ans


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        test_cases = parse_input()
        for i, tc in enumerate(test_cases):
            actual = max_profit(tc[0])
            expected = tc[1]
            self.assertEqual(actual, expected, f"{i} {tc[0]}")

    def test_best_time_to_buy_and_sell_stock0(self):
        test_cases = parse_input()
        for i, tc in enumerate(test_cases):
            actual = max_profit0(tc[0])
            expected = tc[1]
            self.assertEqual(actual, expected, f"{i} {tc[0]}")

    def test_best_time_to_buy_and_sell_stock1(self):
        test_cases = parse_input()
        for i, tc in enumerate(test_cases):
            actual = max_profit1(tc[0])
            expected = tc[1]
            self.assertEqual(actual, expected, f"{i} {tc[0]}")


if __name__ == "__main__":
    unittest.main()
