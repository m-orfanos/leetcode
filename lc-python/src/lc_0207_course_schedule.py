import unittest
from typing import List


def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Time complexity: O(m+n)
    Space complexity: O(m+n)
      where
        m = nb of courses/nodes/vertices
        n = nb of prerequisites/links/edges

    Commentary
      I tried multiples approaches until I found something I liked.

      The first approach consisted of created a graph and then walking
      the graph checking for circular paths. It timed out :D

      For a second approach, I used a nxn matrix to reflect walking
      the graph. I would complete one walk and update it's value,
      one at a time. It also timed out :D :D :D

      Third time's the try! I modified the above approach to cache
      all child traversals. It passed the test but the runtime was
      in the bottom ten percent of submissions. I wanted to find
      another way.

      Eventually I looked at some of the shared solutions: all of
      them use recursion... which I wanted to avoid. But I was stuck
      so I wrote up a recursive approach and tried to convert it
      into an iterative one.

      I got stuck for a long time because I couldn't figure out
      how to convert the base case. I finally understood you can't
      just pop the stack and mutate the state as in a simple DFS
      traversal: you have to wait until all the child nodes have
      been processed. It seems to obvious in hindsight XD
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


class Test(unittest.TestCase):
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

    def test_(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = tc[0]
            b = tc[1]
            expected = tc[2]

            actual = can_finish(a, b)

            self.assertEqual(actual, expected, f"test case {i} failed")


if __name__ == "__main__":
    unittest.main()
