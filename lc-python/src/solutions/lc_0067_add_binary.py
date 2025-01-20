import unittest


def add_binary0(a: str, b: str) -> str:
    """
    Time complexity: O(a+b)
    Space complexity: O(a+b)
    """
    an = int(f"0b{a}", base=0)
    bn = int(f"0b{b}", base=0)
    cn = an + bn
    return bin(cn)[2:]


def add_binary1(a: str, b: str) -> str:
    """
    Time complexity: O(a+b)
    Space complexity: O(a+b)
    """

    def to_int(s: str) -> int:
        base = 2
        ans = 0
        for ch in s:
            digit = 1 if ch == "1" else 0
            ans = ans * base + digit
        return ans

    def to_bin(n: int) -> str:
        if n == 0:
            return "0"
        base = 2
        digits = []
        while n > 0:
            digits.append("1" if n % base == 1 else "0")
            n //= base
        return "".join(digits[::-1])

    aa = to_int(a)
    bb = to_int(b)
    cc = aa + bb

    return to_bin(cc)


def add_binary2(a: str, b: str) -> str:
    """
    Time complexity: O(max(a,b))
    Space complexity: O(max(a,b))
    """
    if len(b) < len(a):
        t = a
        a = b
        b = t

    ans = []
    carry_bit = 0
    n = min(len(a), len(b))

    # add two numbers bit by bit
    # if b > a, ignores the extra bits (if applicable)
    for i in range(n):
        aa = 1 if a[len(a) - 1 - i] == "1" else 0
        bb = 1 if b[len(b) - 1 - i] == "1" else 0
        cc = aa + bb + carry_bit  # 0, 1, 2 or 3

        sum_bit = cc & 0b1
        ans.append("1" if sum_bit == 1 else "0")

        carry_bit = cc >> 0b1

    # add remaining digits of b (if applicable)
    for i in range(n, len(b)):
        bb = 1 if b[len(b) - 1 - i] == "1" else 0
        cc = bb + carry_bit  # 0, 1 or 2

        sum_bit = cc & 0b1
        ans.append("1" if sum_bit == 1 else "0")

        carry_bit = cc >> 0b1

    if carry_bit > 0:
        ans.append("1")

    return "".join(ans[::-1])


class TestAddBinary(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            ["11", "1", "100"],
            ["1010", "1011", "10101"],
            ["0", "0", "0"],
            ["100", "110010", "110110"],
            ["110010", "10111", "1001001"],
        ]
        return data

    def test_add_binary0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            b = tc[1]
            expected = tc[2]

            actual = add_binary0(a, b)

            self.assertEqual(actual, expected)

    def test_add_binary1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            b = tc[1]
            expected = tc[2]

            actual = add_binary1(a, b)

            self.assertEqual(actual, expected)

    def test_add_binary2(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            b = tc[1]
            expected = tc[2]

            actual = add_binary2(a, b)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
