import unittest
from typing import List


def longest_common_prefix0(ws: List[str]) -> str:
    """
    Time complexity: O(kn)
    Space complexity: O(k)

    where
    - n is the number of words, and
    - k is the length of the shortest word
    """
    if len(ws) == 0:
        return ""
    l = min(map(len, ws))
    for i in range(l):
        ch = ws[0][i]
        for w in ws[1:]:
            if ch != w[i]:
                return ws[0][:i]
    # occurs when len(ws) == 1
    return ws[0][:l]


def longest_common_prefix(ws: List[str]) -> str:
    """
    Time complexity: O(kn log n)
    - The sort is O(n log n) but each comparison in the sort is O(k)...
    Space complexity: O(kn)

    where
    - n is the number of words, and
    - k is the length of the shortest word
    """
    if len(ws) == 0:
        return ""

    if len(ws) == 1:
        return ws[0]

    # sort string alphabetically
    ws = sorted(ws)
    word1 = ws[0]
    word2 = ws[-1]

    # compare only the first and last words
    ans = ""
    l = min(len(word1), len(word2))
    for i in range(l):
        if word1[i] != word2[i]:
            break
        ans += word1[i]

    return ans


class TestLongestCommonPrefix(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[], ""],
            [[""], ""],
            [["pewpew"], "pewpew"],
            [["", ""], ""],
            [["flower", "flow", "flight"], "fl"],
            [["dog", "racecar", "car"], ""],
            [["cir", "car"], "c"],
            [["reflower", "flow", "flight"], ""],
        ]
        return data

    def test_longest_common_prefix0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            ws = tc[0]
            expected = tc[1]

            actual = longest_common_prefix0(ws)

            self.assertEqual(actual, expected)

    def test_longest_common_prefix(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            ws = tc[0]
            expected = tc[1]

            actual = longest_common_prefix(ws)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
