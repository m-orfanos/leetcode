import unittest
from collections import deque


def longest_substring0(s: str) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    best = 0
    window = deque()
    chars = {}
    for ch in s:
        while ch in chars:
            chars.pop(window.popleft())

        chars[ch] = 0
        window.append(ch)

        best = max(len(window), best)

    return best


def longest_substring1(s: str) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    letters = [-1] * 128

    best = 0
    left = 0
    for i, ch in enumerate(s):
        if letters[ord(ch)] >= left:
            left = letters[ord(ch)] + 1
        else:
            best = max(best, i - left + 1)
        letters[ord(ch)] = i

    return best


class TestLengthOfLongestSubstring(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            ["abcabcbb", 3],
            ["bbbbb", 1],
            ["pwwkew", 3],
        ]
        return data

    def test_longest_substring0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            actual = longest_substring0(a)

            self.assertEqual(actual, expected, f"{a} {expected}")

    def test_longest_substring1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            actual = longest_substring1(a)

            self.assertEqual(actual, expected, f"{a} {expected}")


if __name__ == "__main__":
    unittest.main()
