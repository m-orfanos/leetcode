import unittest


def longest_palindrome(s: str) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # build histogramme {char:count}
    d = {}
    for ch in s:
        d[ch] = 1 + d.get(ch, 0)

    # if count is even
    #   add chars to string
    # if count is odd
    #   the largest odd chunk will be at the center
    #   all other chunks half to each side
    # if there exists 1 odd chunk
    #   this was the largest chunk
    #   add 1 to length
    ans = 0
    has_odd = False
    for ch in d.keys():
        nb = d[ch]
        if nb % 2 == 1:
            ans += nb - 1
            has_odd = True
        else:
            ans += nb

    if has_odd:
        ans += 1

    return ans


class TestLongestPalindrome(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            ["abccccdd", 7],
            ["a", 1],
        ]
        return data

    def test_longest_palindrome(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            s = tc[0]
            expected = tc[1]

            actual = longest_palindrome(s)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
