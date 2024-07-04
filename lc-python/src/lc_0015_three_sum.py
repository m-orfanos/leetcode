import unittest
from typing import List


def three_sum0(nums: List[int]) -> List[List[int]]:
    """
    Brute-force-ish approach

    Time complexity: O(n^3)
    Space complexity: O(n)
    """
    nums.sort()

    d = {}
    for i in range(len(nums)):
        ni = nums[i]
        if ni not in d:
            d[ni] = []
        d[ni].append(i)

    triplets = []
    ni = None
    nj = None
    for i in range(len(nums)):
        if ni == nums[i]:
            # skip duplicates
            continue
        ni = nums[i]
        for j in range(i + 1, len(nums)):
            if nj == nums[j]:
                # skip duplicates
                continue
            nj = nums[j]
            t = -1 * (ni + nj)
            if t in d:
                for k in d[t]:
                    if i < j < k:
                        nk = nums[k]
                        triplets.append([ni, nj, nk])
                        break

    return triplets


def three_sum1(nums: List[int]) -> List[List[int]]:
    """
    Two-pointer approach

    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    nums.sort()
    triplets = set()
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        target = 0 - nums[i]
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                triplets.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
                # skip duplicates
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

    return list(triplets)


def three_sum2(nums: List[int]) -> List[List[int]]:
    """
    Divide-and-conquer approach, with multiple caches!

    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    # split nums into 3 partitions
    positives = {}
    negatives = {}
    zeroes = 0
    for n in nums:
        if n > 0:
            if n not in positives:
                positives[n] = 0
            positives[n] += 1
        elif n < 0:
            if n not in negatives:
                negatives[n] = 0
            negatives[n] += 1
        else:
            zeroes += 1

    triples = []

    # case (0,n,-n), e.g. 1 positive + 1 negative
    # case (0,-n,n), ignored, it's the mirror of above
    if zeroes > 0:
        for n in positives.keys():
            if -n in negatives:
                triples.append([0, n, -n])
        if zeroes > 2:
            triples.append([0, 0, 0])

    # case (p1,p2,n), e.g. 2 positives + 1 negative
    # case (n1,n2,p), e.g. 2 negatives + 1 positive
    for xs, ys in ((positives, negatives), (negatives, positives)):
        for n1 in xs.keys():
            for n2 in xs.keys():
                if n1 > n2 or (n1 == n2 and xs[n1] < 2):
                    continue
                if -(n1 + n2) in ys:
                    triples.append([n1, n2, -(n1 + n2)])

    # note: the collection does not contain any duplicate values
    return triples


class TestThreeSum(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]],
            [[0, 1, 1], []],
            [[0, 0, 0], [[0, 0, 0]]],
            [
                [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
                [
                    [-4, -2, 6],
                    [-4, 0, 4],
                    [-4, 1, 3],
                    [-4, 2, 2],
                    [-2, -2, 4],
                    [-2, 0, 2],
                ],
            ],
            [
                [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4],
                [
                    [-4, 0, 4],
                    [-4, 1, 3],
                    [-3, -1, 4],
                    [-3, 0, 3],
                    [-3, 1, 2],
                    [-2, -1, 3],
                    [-2, 0, 2],
                    [-1, -1, 2],
                    [-1, 0, 1],
                ],
            ],
        ]
        return data

    @staticmethod
    def sort_collection(xs):
        return sorted(list(map(lambda t: sorted([t[0], t[1], t[2]]), xs)))

    def test_three_sum0(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = tc[0]
            expected = sorted(tc[1])

            actual = self.sort_collection(three_sum0(a))

            self.assertEqual(actual, expected, f"three_sum0 - test case {i}")

    def test_three_sum1(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = tc[0]
            expected = sorted(tc[1])

            actual = self.sort_collection(three_sum1(a))

            self.assertEqual(actual, expected, f"three_sum1 - test case {i}")

    def test_three_sum2(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = tc[0]
            expected = sorted(tc[1])

            actual = self.sort_collection(three_sum2(a))

            self.assertEqual(actual, expected, f"three_sum2 - test case {i}")


if __name__ == "__main__":
    unittest.main()
