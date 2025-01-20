import unittest
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    """
    Time complexity: O(n*m)
    Space complexity: O(n*m)
    """
    m = len(grid)
    n = len(grid[0])

    # EMPTY = 0
    FRESH = 1
    ROTTN = 2

    has_rotted = False
    batch = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == FRESH:
                batch.append((i, j))
            if grid[i][j] == ROTTN:
                has_rotted = True

    mins = 0
    while has_rotted:
        # elapse 1 min, check for new rotten
        rottn = []
        fresh = []
        for x, y in batch:
            is_fresh = True
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    is_fresh = is_fresh and grid[x + dx][y + dy] != ROTTN
            if is_fresh:
                fresh.append((x, y))
            else:
                rottn.append((x, y))

        # update grid
        for x, y in rottn:
            grid[x][y] = ROTTN

        # update state for next iteration
        # update `mins` only if newly rotten, otherwise this iteration
        # would not have been required
        batch = fresh
        if len(rottn) > 0:
            has_rotted = True
            mins += 1
        else:
            has_rotted = False

    return mins if len(batch) == 0 else -1


class TestRottingOranges(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4],
            [[[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1],
            [[[0, 2]], 0],
        ]
        return data

    def test_oranges_rotting(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = tc[0]
            expected = tc[1]

            actual = oranges_rotting(a)

            self.assertEqual(actual, expected, f"test case {i} failed")


if __name__ == "__main__":
    unittest.main()
