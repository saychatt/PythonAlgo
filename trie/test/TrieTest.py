import unittest

from trie.Trie import Trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search_single_word(self):
        self.trie.insert("cat")
        self.assertTrue(self.trie.search("cat"))
        self.assertFalse(self.trie.search("dog"))

    def test_search_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))

    def test_search_nonexistent_word(self):
        self.assertFalse(self.trie.search("missing"))

    def test_partial_word_not_found(self):
        self.trie.insert("hello")
        self.assertFalse(self.trie.search("hell"))

    def test_starts_with_existing_prefix(self):
        self.trie.insert("hello")
        self.assertTrue(self.trie.startsWith("hell"))
        self.assertTrue(self.trie.startsWith("h"))

    def test_starts_with_nonexistent_prefix(self):
        self.assertFalse(self.trie.startsWith("xyz"))

    def test_multiple_words_same_prefix(self):
        words = ["cat", "car", "card"]
        for word in words:
            self.trie.insert(word)

        for word in words:
            self.assertTrue(self.trie.search(word))
        self.assertTrue(self.trie.startsWith("ca"))

    def test_overlapping_words(self):
        self.trie.insert("app")
        self.trie.insert("apple")

        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.startsWith("app"))


if __name__ == '__main__':
    unittest.main()