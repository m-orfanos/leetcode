import unittest
from typing import List


def flood_fill(
    image: List[List[int]], row: int, col: int, color: int
) -> List[List[int]]:
    """
    Time complexity: O(n*m)
    Space complexity: O(n*m)
    """
    image_copy = [xs[:] for xs in image]
    color_old = image_copy[row][col]

    # depth-first graph traversal
    to_fill = [(row, col)]
    while len(to_fill) > 0:
        (x, y) = to_fill.pop()

        if image_copy[x][y] != color_old or image_copy[x][y] == color:
            continue

        image_copy[x][y] = color

        if x > 0:
            to_fill.append((x - 1, y))
        if x < len(image_copy) - 1:
            to_fill.append((x + 1, y))
        if y > 0:
            to_fill.append((x, y - 1))
        if y < len(image_copy[x]) - 1:
            to_fill.append((x, y + 1))

    return image_copy


class TestFloodFill(unittest.TestCase):

    def test_flood_fill(self):
        test_cases = [
            [
                [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
                1,
                1,
                2,
                [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
            ],
            [[[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]],
        ]
        for i, tc in enumerate(test_cases):
            actual = flood_fill(tc[0], tc[1], tc[2], tc[3])
            expected = tc[4]
            self.assertEqual(actual, expected, f"{i} {tc}")


if __name__ == "__main__":
    unittest.main()
