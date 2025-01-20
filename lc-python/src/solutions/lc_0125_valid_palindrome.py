import unittest


def is_palindrome(s: str) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    t = [ch.lower() for ch in s if ch.isalnum()]
    return t == t[::-1]


def is_palindrome0(s: str) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    lhs = 0
    rhs = len(s) - 1

    while lhs <= rhs:
        if not s[lhs].isalnum():
            lhs += 1
            continue
        if not s[rhs].isalnum():
            rhs -= 1
            continue
        if s[lhs].lower() != s[rhs].lower():
            return False
        lhs += 1
        rhs -= 1

    return True


class TestValidPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        test_cases = [
            ["A man, a plan, a canal: Panama", True],
            ["race a car", False],
            [" ", True],
            ["1b1", True],
            ["0P", False],
        ]
        for tc in test_cases:
            expected = tc[1]
            actual = is_palindrome(tc[0])
            self.assertEqual(actual, expected)

    def test_is_palindrome0(self):
        test_cases = [
            ["A man, a plan, a canal: Panama", True],
            ["race a car", False],
            [" ", True],
            ["1b1", True],
            ["0P", False],
        ]
        for tc in test_cases:
            expected = tc[1]
            actual = is_palindrome0(tc[0])
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
