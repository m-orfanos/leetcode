import unittest


def climb_stairs(n: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # bottom-up approach
    step1 = 0
    step2 = 1
    while n > 0:
        t = step1
        step1 = step2
        step2 += t

        n -= 1

    return step2


def climb_stairs_recursive(n: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """

    # top-down approach
    def nb_steps(n):
        if n < 1:
            return 0
        elif n == 1 or n == 2:
            return n
        else:
            return nb_steps(n - 1) + nb_steps(n - 2)

    return nb_steps(n)


def climb_stairs_combinatorics(n: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    mem_fact = {}
    mem_comb = {}

    def fact(i):
        # early exits
        if i in mem_fact:
            return mem_fact[i]
        if i == 0 or i == 1:
            mem_fact[i] = 1
            return 1

        # compute fact
        mem_fact[i] = i * fact(i - 1)
        return mem_fact[i]

    def comb(n, k):
        # early exits
        if (n, k) in mem_comb:
            return mem_comb[(n, k)]
        if n == k or k == 0:
            mem_comb[(n, k)] = 1
            return 1
        if k == 1:
            mem_comb[(n, k)] = n
            return n

        # compute multinomial coefficient
        # nCk = n!/k!/(n-k)!
        mem_comb[(n, k)] = fact(n) // fact(k) // fact(n - k)
        return mem_comb[(n, k)]

    ans = 0
    rs = {1: n, 2: 0}
    while rs[1] >= 0:
        ans += comb(rs[1] + rs[2], rs[1])
        rs[1] -= 2
        rs[2] += 1

    return ans


class TestClimbingStairs(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 5],
            [5, 8],
            [6, 13],
        ]
        return data

    def test_climbing_stairs_combinatorics(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            n = tc[0]
            expected = tc[1]

            actual = climb_stairs_combinatorics(n)

            self.assertEqual(actual, expected)

    def test_climbing_stairs_recursive(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            n = tc[0]
            expected = tc[1]

            actual = climb_stairs_recursive(n)

            self.assertEqual(actual, expected)

    def test_climbing_stairs_iterative(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            n = tc[0]
            expected = tc[1]

            actual = climb_stairs(n)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
