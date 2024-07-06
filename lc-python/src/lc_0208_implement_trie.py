import unittest


class Trie:

    def __init__(self):
        self.g = [-1, {}]
        self.n = 0

    def insert(self, word: str) -> None:
        """
        Time complexity: O(k)
        Space complexity: O(k)
        """
        if len(word) <= 0:
            return

        curr = self.g
        for ch in word:
            _, d = curr
            if ch not in d:
                d[ch] = [-1, {}]
            curr = d[ch]

        v, _ = curr
        if v < 0:
            curr[0] = self.n
            self.n += 1

    def search(self, word: str) -> bool:
        """
        Time complexity: O(k)
        Space complexity: O(1)
        """
        curr = self.g
        for ch in word:
            _, d = curr
            if ch not in d:
                return False
            curr = d[ch]

        v, _ = curr
        return v >= 0

    def startsWith(self, prefix: str) -> bool:
        """
        Time complexity: O(k)
        Space complexity: O(1)
        """
        curr = self.g
        for ch in prefix:
            _, d = curr
            if ch not in d:
                return False
            curr = d[ch]

        return True


class TestImplementTrie(unittest.TestCase):
    def test_implement_trie(self):
        trie = Trie()
        trie.insert("apple")

        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))

        trie.insert("app")

        self.assertTrue(trie.startsWith("app"))


if __name__ == "__main__":
    unittest.main()
