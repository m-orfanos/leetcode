import unittest


def hamming_weight0(n: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    cnt = 0
    while n > 0:
        cnt += n % 2
        n //= 2
    return cnt


def hamming_weight(n: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # pointless bit fiddling that should be optimized by
    # the compiler/interpreter imo
    cnt = 0
    while n > 0:
        cnt += n & 1
        n >>= 1
    return cnt


class TestProblemName(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [11, 3],
            [128, 1],
            [2147483645, 30],
        ]
        return data

    def test_number_one_bits0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            n = tc[0]
            expected = tc[1]

            actual = hamming_weight0(n)

            self.assertEqual(actual, expected)

    def test_number_one_bits(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            n = tc[0]
            expected = tc[1]

            actual = hamming_weight(n)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
