import unittest
import sys
from typing import List
from collections import deque


def update_matrix0(mat: List[List[int]]) -> List[List[int]]:
    """
    Time complexity: O(m^2 x n^2)
    Space complexity: O(mxn)
    """

    ans = [[sys.maxsize] * len(mat[i]) for i in range(len(mat))]
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y] == 0:
                for i in range(len(mat)):
                    for j in range(len(mat[i])):
                        dist = abs(x - i) + abs(y - j)
                        ans[i][j] = min(ans[i][j], dist)

    return ans


def update_matrix1(mat: List[List[int]]) -> List[List[int]]:
    """
    Time complexity: O(mxn)
    Space complexity: O(mxn)
    """
    nrows = len(mat)
    ncols = len(mat[0])

    # store all the 0-valued cells into a queue
    # set all over values in the matrix to the max integer
    q = deque()
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y] == 0:
                q.append([x, y])
            else:
                mat[x][y] = sys.maxsize

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # perform a BFS across the matrix with 0-valued cells as entry points
    # important! cells may be visited multiple times
    while len(q) > 0:
        [x, y] = q.popleft()

        # visit neighbors around (x,y)
        for [dx, dy] in directions:
            xn = x + dx
            yn = y + dy
            if 0 <= xn < nrows and 0 <= yn < ncols and mat[xn][yn] > mat[x][y] + 1:
                # update the distance of this neighbor to a 0-valued cell
                # cells needs to be traversed again each time there's an update
                mat[xn][yn] = mat[x][y] + 1
                q.append([xn, yn])

    return mat


class TestUpdateMatrix(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [
                [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ],
            [
                [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
                [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
            ],
            [
                [
                    [0, 1, 0, 1, 0],
                    [1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 1],
                    [0, 1, 0, 1, 0],
                ],
                [
                    [0, 1, 0, 1, 0],
                    [1, 2, 1, 2, 1],
                    [2, 1, 0, 1, 2],
                    [1, 2, 1, 2, 1],
                    [0, 1, 0, 1, 0],
                ],
            ],
        ]
        return data

    def test_update_matrix0(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            nums = tc[0]
            expected = tc[1]

            actual = update_matrix0(nums)

            self.assertEqual(actual, expected, f"update_matrix0, test case #{i}")

    def test_update_matrix1(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            nums = tc[0]
            expected = tc[1]

            actual = update_matrix1(nums)

            self.assertEqual(actual, expected, f"update_matrix1, test case #{i}")


if __name__ == "__main__":
    unittest.main()
