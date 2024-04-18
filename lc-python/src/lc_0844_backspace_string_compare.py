import unittest


def backspace_string_compare_naive(s: str, t: str) -> bool:
    """
    Time complexity: O(m+n)
    Space complexity: O(m+n)
    """

    def cleanup(xs: str):
        ans = []
        for ch in xs:
            if ch == "#":
                if len(ans) > 0:
                    ans.pop()
            else:
                ans.append(ch)
        return "".join(ans)

    ss = cleanup(s)
    tt = cleanup(t)

    return ss == tt


def backspace_string_compare(s: str, t: str) -> bool:
    """
    Time complexity: O(m+n)
    Space complexity: O(1)
    """

    def next(s: str, i: int) -> int:
        cnt = 0
        while i >= 0:
            if s[i] == "#":
                i -= 1
                cnt += 1
                continue
            if cnt > 0:
                i -= 1
                cnt -= 1
                continue
            return i
        return -1

    si = len(s) - 1
    ti = len(t) - 1
    while si >= 0 and ti >= 0:
        si = next(s, si)
        ti = next(t, ti)
        if si < 0 or ti < 0:
            break
        if s[si] != t[ti]:
            return False
        si -= 1
        ti -= 1

    if si >= 0 and s[si] == "#":
        si = next(s, si)
    if ti >= 0 and t[ti] == "#":
        ti = next(t, ti)

    return si < 0 and ti < 0


class TestBackspaceStringCompare(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            ["ab#c", "ad#c", True],
            ["ab##", "c#d#", True],
            ["a#c", "b", False],
            ["gtc#uz#", "gtcm##uz#", True],
            ["a##c", "#a#c", True],
            ["y#fo##f", "y#f#o##f", True],
            ["bxj##tw", "bxo#j##tw", True],
            ["bxj##tw", "bxj###tw", False],
            ["nzp#o#g", "b#nzp#o#g", True],
        ]
        return data

    def test_backspace_string_compare_naive(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            s = tc[0]
            t = tc[1]
            expected = tc[2]

            actual = backspace_string_compare_naive(s, t)

            self.assertEqual(actual, expected)

    def test_backspace_string_compare(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            s = tc[0]
            t = tc[1]
            expected = tc[2]

            actual = backspace_string_compare(s, t)

            self.assertEqual(actual, expected, f"{s} {t}")


if __name__ == "__main__":
    unittest.main()
