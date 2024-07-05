import unittest
from typing import List


def eval_rpn0(tokens: List[str]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            # can avoid the second pop in favour
            # of mutating the entry directly but wtv
            r = stack.pop()
            l = stack.pop()
            if token == "+":
                stack.append(l + r)
            elif token == "-":
                stack.append(l - r)
            elif token == "*":
                stack.append(l * r)
            else:  # elif token == "/":
                stack.append(int(l / r))

    return stack.pop()


class TestEvaluateReversePolishNotation(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [["2", "1", "+", "3", "*"], 9],
            [["4", "13", "5", "/", "+"], 6],
            [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22],
        ]
        return data

    def test_evaluate_reverse_polish_notation0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            actual = eval_rpn0(a)

            self.assertEqual(actual, expected, f"{a} {expected}")


if __name__ == "__main__":
    unittest.main()
