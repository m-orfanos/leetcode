import unittest
from typing import List


def can_finish0(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Time complexity: O(m+n)
    Space complexity: O(m+n)
      where
        m = nb of courses/nodes/vertices
        n = nb of prerequisites/links/edges
    """

    adjacents = [[] for _ in range(numCourses)]
    for [course, prerequisite] in prerequisites:
        adjacents[prerequisite].append(course)

    TODO = 0
    DOING = -1
    DONE = 1
    state = [TODO] * numCourses

    for i in range(numCourses):
        s = [i]
        while s:
            n = s[-1]
            if state[n] == DONE:
                s.pop()
                continue
            state[n] = DOING

            # add prereqs if not completed
            cnt = len(s)
            for adj in adjacents[n]:
                if state[adj] == DOING:
                    return False
                if state[adj] == TODO:
                    s.append(adj)

            # pop stack only if all prereqs completed
            if len(s) - cnt == 0:
                s.pop()
                state[n] = DONE

    return True


class TestCourseSchedule(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [2, [[1, 0]], True],
            [2, [[1, 0], [0, 1]], False],
            [4, [[0, 1], [1, 2], [2, 3], [2, 0]], False],
            [4, [[1, 0], [2, 0], [3, 1], [3, 2]], True],
            [7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]], True],
        ]
        return data

    def test_can_finish0(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = tc[0]
            b = tc[1]
            expected = tc[2]

            actual = can_finish0(a, b)

            self.assertEqual(actual, expected, f"test case {i} failed")


if __name__ == "__main__":
    unittest.main()
