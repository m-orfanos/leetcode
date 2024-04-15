import unittest


def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Time complexity: O(n)

    Space complexity: O(1)
    While we build a map, it's essentially O(1) since the map is a histogram
    of English letters to a count.
    """
    if len(ransomNote) > len(magazine):
        return False

    letters = {}
    for ch in magazine:
        letters[ch] = letters.get(ch, 0) + 1

    for ch in ransomNote:
        if letters.get(ch, 0) > 0:
            letters[ch] -= 1
        else:
            return False

    return True


class TestRansomNote(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            ["a", "b", False],
            ["aa", "ab", False],
            ["aa", "aab", True],
        ]
        return data

    def test_ransom_note(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            b = tc[1]
            expected = tc[2]

            actual = can_construct(a, b)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
