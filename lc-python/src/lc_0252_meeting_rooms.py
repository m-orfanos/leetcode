import unittest
from typing import List, Tuple


def can_attend_naive(meetings: List[List[int]]) -> bool:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """

    def has_overlap(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> bool:
        lhs = max(interval1[0], interval2[0])
        rhs = min(interval1[1], interval2[1])
        return lhs <= rhs

    # need to determine if meetings overlap
    for i in range(len(meetings)):
        meeting1 = meetings[i]
        for j in range(i + 1, len(meetings)):
            meeting2 = meetings[j]
            if has_overlap(meeting1, meeting2):
                return False
    return True


def can_attend(meetings: List[List[int]]) -> bool:
    """
    Time complexity: O(n log n)
    Space complexity: O(log n)
    """
    # need to determine if meetings overlap

    # sort by start time
    meetings.sort(key=lambda x: x[0])

    for i in range(1, len(meetings)):
        meeting1_end = meetings[i - 1][1]
        meeting2_start = meetings[i][0]
        if meeting1_end > meeting2_start:
            return False

    return True


class TestMeetingRooms(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[[0, 30], [5, 10], [15, 20]], False],
            [[[7, 10], [2, 4]], True],
        ]
        return data

    def test_meeting_rooms0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = tc[0]
            expected = tc[1]

            actual = can_attend_naive(xs)

            self.assertEqual(actual, expected)

    def test_meeting_rooms(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = tc[0]
            expected = tc[1]

            actual = can_attend(xs)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
