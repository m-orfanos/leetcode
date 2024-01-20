import os
import pathlib

from typing import List


def chunks(l: List, n: int) -> List[List]:
    """
    Splits list 'l' into 'n'-sized chunks.
    Example
      Input: chunks([1, 2, 3, 4], 2)
      Output: [[1, 2], [3, 4]]
    """
    return [l[i : i + n] for i in range(0, len(l), n)]


def to_list_int(s: str) -> List[int]:
    """
    Parses 's' as a list of integers.
    Assumes format is "[1, 2, 3]".
    """
    return list(map(int, s[1:-1].split(",")))


def read_lines(filename: str) -> List[str]:
    """
    Retrieves the file pointed to by 'filename' and reads
    its contents as a list of strings.
    """
    path = os.path.join(os.path.dirname(__file__), filename)
    file = pathlib.Path(f"{path}")
    with open(file) as f:
        lines = f.read().splitlines()
    return lines
