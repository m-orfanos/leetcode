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


if __name__ == "__main__":
    unittest.main()
