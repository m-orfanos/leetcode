import unittest


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            min_val = self.stack[-1][1]
        else:
            min_val = val
        min_val = min(val, min_val)

        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class TestMinStack(unittest.TestCase):
    def test_min_stack(self):
        s = MinStack()
        s.push(-2)
        s.push(0)
        s.push(-3)

        self.assertEqual(s.getMin(), -3)
        s.pop()
        self.assertEqual(s.top(), 0)
        self.assertEqual(s.getMin(), -2)


if __name__ == "__main__":
    unittest.main()
