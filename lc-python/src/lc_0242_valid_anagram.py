import unittest


def is_anagram(s: str, t: str) -> bool:
    # create map from s {char:count}
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    # decrement map count depending on t
    for ch in t:
        if ch in d:
            d[ch] -= 1
        else:
            # char does not exist in s
            return False

    # validate all chars have been used
    return all(map(lambda x: x == 0, d.values()))


class TestValidAnagram(unittest.TestCase):
    def test_is_anagram(self):
        test_cases = [
            ["anagram", "nagaram", True],
            ["rat", "car", False],
        ]
        for tc in test_cases:
            self.assertEqual(is_anagram(tc[0], tc[1]), tc[2])


if __name__ == "__main__":
    unittest.main()
