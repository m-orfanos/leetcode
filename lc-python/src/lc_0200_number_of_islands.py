import unittest
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """
    Time complexity: O(n*m)
    Space complexity: O(n*m)
    """
    n = len(grid)
    m = len(grid[0])

    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                s = [(i, j)]
                while s:
                    x, y = s.pop()
                    if grid[x][y] != "1":
                        continue
                    grid[x][y] = cnt
                    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        if 0 <= x + dx < n and 0 <= y + dy < m:
                            s.append((x + dx, y + dy))
                cnt += 1

    return cnt


class TestNumberOfIslands(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ],
                1,
            ],
            [
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ],
                3,
            ],
        ]
        return data

    def test_number_of_islands(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = tc[0]
            expected = tc[1]

            actual = num_islands(a)

            self.assertEqual(actual, expected, f"test case {i} failed")


if __name__ == "__main__":
    unittest.main()
