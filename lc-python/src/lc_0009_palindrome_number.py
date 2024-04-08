import unittest


def is_palindrome0(x: int) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if x < 0:
        return False
    rev = 0
    copy = x
    while copy > 0:
        rev = 10 * rev + copy % 10
        copy //= 10
    return x == rev


def is_palindrome1(x: int) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    # even-length numbers
    #        x  rev
    # 12344321    0
    #  1234432    1
    #   123443   12
    #    12344  123
    #     1234 1234 <-- compare directly
    #
    # odd-length numbers
    #     x   rev
    # 12321     0
    #  1232     1
    #   123    12
    #    12   123 <-- drop last digit
    rev = 0
    while rev < x:
        rev = 10 * rev + x % 10
        x //= 10
    return x == rev or x == rev // 10


class TestPalindromeNumber(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [1221, True],
            [121, True],
            [-121, False],
            [10, False],
        ]
        return data

    def test_is_palindrome0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            actual = is_palindrome0(a)

            self.assertEqual(actual, expected)

    def test_is_palindrome1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            actual = is_palindrome1(a)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
