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


if __name__ == "__main__":
    unittest.main()
