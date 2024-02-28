import math

from typing import List


def chunks(l: List, n: int) -> List[List]:
    """
    Splits list 'l' into 'n'-sized chunks.
    Example
      Input: chunks([1, 2, 3, 4], 2)
      Output: [[1, 2], [3, 4]]
    """
    return [l[i: i + n] for i in range(0, len(l), n)]


def to_list_int(s: str) -> List[int]:
    """
    Parses 's' as a list of integers.
    Assumes format is "[1, 2, 3]".
    """
    if s == "[]":
        return []
    return list(map(int, s[1:-1].split(",")))


def max_subarray(xs: List[int]) -> int:
    """
    Find the largest sum of any contiguous subarray.
    Kadane's algorithm (maximum subarray problem)
    """
    best_sum = -math.inf
    current_sum = 0
    for x in xs:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
