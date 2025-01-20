import unittest
from typing import List


def roman_to_integer(s: str) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    adjust = {
        ("I", "V"): 2,
        ("I", "X"): 2,
        ("X", "L"): 20,
        ("X", "C"): 20,
        ("C", "D"): 200,
        ("C", "M"): 200,
    }

    ans = 0
    for i in range(0, len(s) - 1):
        ans += symbols[s[i]]
        # adjust if next character forms a IV, IX, etc. pattern
        ans -= adjust.get((s[i], s[i + 1]), 0)

    # last digit
    ans += symbols[s[len(s) - 1]]

    return ans


class TestRomanToInteger(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            ["III", 3],
            ["LVIII", 58],
            ["MCMXCIV", 1994],
        ]
        return data

    def test_roman_to_integer(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            s = tc[0]
            expected = tc[1]

            actual = roman_to_integer(s)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
