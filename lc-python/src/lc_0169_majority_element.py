import unittest
from typing import List


def majority_element(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    counter = {}
    for n in nums:
        cnt = 1 + counter.get(n, 0)
        if cnt > len(nums) // 2:
            return n
        counter[n] = cnt
    return -1


def majority_element_boyer_moore(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # Boyer–Moore majority vote algorithm
    # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
    cnt = 1
    majority = nums[0]
    for n in nums[1:]:
        if n == majority:
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            majority = n
            cnt = 1
    return majority


def majority_element_boyer_moore_multi(nums: List[int], nb_bags: int) -> List[int]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # modified Boyer–Moore majority vote algorithm
    # instead of the majority, returns "nb_bags" majority
    # NOTE: if there aren't "nb_bags" distinct elements, returns as many as possible (up to "nb_bags")
    # NOTE: this approach CANNOT know which of the bags is the biggest
    # https://cs.stackexchange.com/questions/91803/explaination-for-variation-of-boyer-moore-majority-voting-algorithm
    bags = {}
    for n in nums:
        # if there is a container containing n, add it to it
        if n in bags:
            bags[n] += 1

        if len(bags.keys()) < nb_bags:
            # if there is no container containing n AND there is an empty container
            # add it to an empty container
            bags[n] = 1
        else:
            # if there is no container containing n AND there are no empty containers
            # remove 1 element from EVERY container
            to_delete = []
            for k in bags.keys():
                if bags[k] >= 1:
                    bags[k] -= 1
                else:
                    to_delete.append(k)
            for k in to_delete:
                del bags[k]

    # bags sort by value
    bags = {k: v for k, v in sorted(bags.items(), key=lambda item: item[1])}
    return sorted(list(bags.keys()))


class TestMajorityElement(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[3, 2, 3], 3],
            [[2, 2, 1, 1, 1, 2, 2], 2],
        ]
        return data

    def test_majority_element(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = tc[0]
            expected = tc[1]

            actual = majority_element(xs)

            self.assertEqual(actual, expected)

    def test_majority_element_boyer_moore(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = tc[0]
            expected = tc[1]

            actual = majority_element_boyer_moore(xs)

            self.assertEqual(actual, expected)

    def test_majority_element_boyer_moore_multi(self):
        test_cases = [
            [[3, 2, 3], [2, 3]],
            [[2, 2, 1, 1, 1, 2, 2], [1, 2]],
            [[2, 2, 1, 1, 1, 2, 2, 3], [1, 2, 3]],
        ]
        for tc in test_cases:
            xs = tc[0]
            expected = tc[1]

            actual = majority_element_boyer_moore_multi(xs, len(expected))

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
