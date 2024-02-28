import string
import unittest


def is_palindrome(s: str) -> bool:
    digits = list(map(lambda n: str(n), range(10)))
    t = ""
    for ch in s:
        if ch in string.ascii_lowercase:
            t += ch
        elif ch in string.ascii_uppercase:
            t += ch.lower()
        elif ch in digits:
            t += ch
    return t == t[::-1]


class TestValidPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        test_cases = [
            ["A man, a plan, a canal: Panama", True],
            ["race a car", False],
            [" ", True],
            ["1b1", True]
        ]
        for tc in test_cases:
            self.assertEqual(is_palindrome(tc[0]), tc[1])


if __name__ == "__main__":
    unittest.main()
