from trie.TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Inserts the string word into the prefix
    # Assumes the string is a valid word.
    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            #check if the char exists in any of the children
            if char not in cur.children:
                cur.children[char] = TrieNode()
            #move to the child
            cur = cur.children[char]
        cur.endOfWord = True

    # Returns true if the string word is in the prefix tree
    # (i.e., was inserted before), and false otherwise.
    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            #if any of the char not exists in children return False
            if char not in cur.children:
                return False
            cur = cur.children[char]
        #Return the value, if it's a word it will be true.
        return cur.endOfWord

    #Returns true if there is a previously inserted
    # string word that has the prefix prefix, and false otherwise.
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True












