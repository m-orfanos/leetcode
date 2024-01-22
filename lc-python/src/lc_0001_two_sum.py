from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Instead of checking for pairs of entries, iterate over the array
    once and check if there is a matching entry that satisfies the target.

    Requires a map to be built from the initial array. Can also be built
    just-in-time instead of pre-computed (not done below).

    Time complexity: O(n)
    Space complexity: O(n)
    """
    nums_dict = {n: i for (i, n) in enumerate(nums)}
    for i, n in enumerate(nums):
        m = target - n
        if m in nums_dict and nums_dict[m] != i:
            return [i, nums_dict[m]]
    # no solution found, should not happen
    return []


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Search for target by checking pairs of entries in the list. At worst
    every possible entry pair will be checked.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    # no solution found, should not happen
    return []
