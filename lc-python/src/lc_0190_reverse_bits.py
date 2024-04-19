import unittest


def reverse_bits(n: int) -> int:
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    rev = 0
    for _ in range(32):
        rev = rev << 1 | (n & 0b1)
        n = n >> 1
    return rev


def reverse_bits1(n: int) -> int:
    # 00000010100101000001111010011100
    #       10100101000001111010011100 = bin(43261596)
    # note the missing leading zeros
    rev = 0
    for _ in range(32):
        rev = 2 * rev + n % 2
        n //= 2
    return rev


class TestReverseBits(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [43261596, 964176192],
            [4294967293, 3221225471],
        ]
        return data

    def test_reverse_bits(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            actual = reverse_bits(a)

            self.assertEqual(actual, expected)

    def test_reverse_bits1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            actual = reverse_bits1(a)

            self.assertEqual(actual, expected, f"{a} {expected}")


if __name__ == "__main__":
    unittest.main()
