import unittest


class MyQueue:
    def __init__(self):
        self.writer = []
        self.reader = []

    def push(self, x: int) -> None:
        if self._was_reading():
            self._move_to_writer()
        self.writer.append(x)

    def pop(self) -> int:
        if self._was_writing():
            self._move_to_reader()
        return self.reader.pop()

    def peek(self) -> int:
        if self._was_writing():
            self._move_to_reader()
        return self.reader[len(self.reader) - 1]

    def empty(self) -> bool:
        return len(self.writer) + len(self.reader) == 0

    def _was_writing(self) -> bool:
        return len(self.writer) > 0

    def _was_reading(self) -> bool:
        return len(self.reader) > 0

    def _move_to_writer(self) -> None:
        while len(self.reader) > 0:
            self.writer.append(self.reader.pop())

    def _move_to_reader(self) -> None:
        while len(self.writer) > 0:
            self.reader.append(self.writer.pop())


class TestImplementQueueUsingStack(unittest.TestCase):
    def test_implement_queue_using_stack(self):
        q = MyQueue()

        q.push(1)
        self.assertEqual(q.writer, [1])
        self.assertEqual(q.reader, [])

        q.push(2)
        self.assertEqual(q.writer, [1, 2])
        self.assertEqual(q.reader, [])

        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.writer, [])
        self.assertEqual(q.reader, [2, 1])

        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.writer, [])
        self.assertEqual(q.reader, [2])

        self.assertFalse(q.empty())
        self.assertEqual(q.writer, [])
        self.assertEqual(q.reader, [2])


if __name__ == "__main__":
    unittest.main()
