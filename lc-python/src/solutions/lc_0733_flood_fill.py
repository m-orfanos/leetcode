import unittest
from typing import List


def flood_fill0(
    image: List[List[int]], row: int, col: int, color: int
) -> List[List[int]]:
    """
    Time complexity: O(n*m)
    Space complexity: O(n*m)
    """
    # https://en.wikipedia.org/wiki/Flood_fill#Stack-based_recursive_implementation_(four-way)
    color_old = image[row][col]

    # depth-first graph traversal
    to_fill = [(row, col)]
    while len(to_fill) > 0:
        x, y = to_fill.pop()

        if image[x][y] != color_old or image[x][y] == color:
            continue

        image[x][y] = color

        # next valid pixel
        if x > 0:
            to_fill.append((x - 1, y))
        if x < len(image) - 1:
            to_fill.append((x + 1, y))
        if y > 0:
            to_fill.append((x, y - 1))
        if y < len(image[x]) - 1:
            to_fill.append((x, y + 1))

    return image


def flood_fill1(
    image: List[List[int]], row: int, col: int, color: int
) -> List[List[int]]:
    def dfs(x: int, y: int) -> None:
        if image[x][y] != color_old or image[x][y] == color:
            return

        image[x][y] = color

        # next valid pixel
        if x > 0:
            dfs(x - 1, y)
        if x < len(image) - 1:
            dfs(x + 1, y)
        if y > 0:
            dfs(x, y - 1)
        if y < len(image[x]) - 1:
            dfs(x, y + 1)

    color_old = image[row][col]

    dfs(row, col)

    return image


class TestFloodFill(unittest.TestCase):

    @staticmethod
    def parse_input():
        data = [
            [
                [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
                1,
                1,
                2,
                [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
            ],
            [[[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]],
        ]
        return data

    def test_flood_fill0(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            actual = flood_fill0(tc[0], tc[1], tc[2], tc[3])
            expected = tc[4]
            self.assertEqual(actual, expected, f"{i} {tc}")

    def test_flood_fill1(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            actual = flood_fill1(tc[0], tc[1], tc[2], tc[3])
            expected = tc[4]
            self.assertEqual(actual, expected, f"{i} {tc}")


if __name__ == "__main__":
    unittest.main()
