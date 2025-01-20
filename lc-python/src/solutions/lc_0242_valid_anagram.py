import unittest
from collections import defaultdict


def is_anagram0(s: str, t: str) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if len(s) != len(t):
        return False

    d = defaultdict(int)
    for i in range(len(s)):
        d[s[i]] += 1
        d[t[i]] -= 1

    return all(map(lambda x: x == 0, d.values()))


def is_anagram1(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


class TestValidAnagram(unittest.TestCase):

    @staticmethod
    def parse_input():
        data = [
            ["anagram", "nagaram", True],
            ["rat", "car", False],
        ]
        return data

    def test_is_anagram0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            self.assertEqual(is_anagram0(tc[0], tc[1]), tc[2])

    def test_is_anagram1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            self.assertEqual(is_anagram1(tc[0], tc[1]), tc[2])


if __name__ == "__main__":
    unittest.main()
