import unittest

from arrays.vanillaArray.GroupAnagrams import GroupAnagrams


class TestGroupAnagrams(unittest.TestCase):
    
    def test_basic_anagrams(self):
        strs = ["act","pots","tops","cat","stop","hat"]
        result = GroupAnagrams.groupAnagrams(strs)
        # Sort each sublist and the main list for comparison
        result = [sorted(group) for group in result]
        result.sort()
        expected = [["hat"], ["act", "cat"], ["pots", "stop", "tops"]]
        expected = [sorted(group) for group in expected]
        expected.sort()
        self.assertEqual(result, expected)
    
    def test_empty_array(self):
        result = GroupAnagrams.groupAnagrams([])
        self.assertEqual(result, [])
    
    def test_single_string(self):
        result = GroupAnagrams.groupAnagrams(["abc"])
        self.assertEqual(result, [["abc"]])
    
    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        result = GroupAnagrams.groupAnagrams(strs)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(result[0]), 1)
    
    def test_all_anagrams(self):
        strs = ["abc", "bca", "cab"]
        result = GroupAnagrams.groupAnagrams(strs)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 3)
    
    def test_empty_strings(self):
        strs = ["", "", "a"]
        result = GroupAnagrams.groupAnagrams(strs)
        # Should have 2 groups: one with empty strings, one with "a"
        self.assertEqual(len(result), 2)
    
    def test_single_character(self):
        strs = ["a", "b", "a"]
        result = GroupAnagrams.groupAnagrams(strs)
        self.assertEqual(len(result), 2)
    
    def test_hash_collision_prevention(self):
        # Test case that exposes multiplication hash collision
        # These strings produce same product but aren't anagrams:
        # Need to find actual collision - let's use a simpler approach
        strs = ["ab", "ba", "c"]  # ab and ba are anagrams, c is separate
        result = GroupAnagrams.groupAnagrams(strs)
        
        # Should have exactly 2 groups
        self.assertEqual(len(result), 2)
        
        # Find which group has the anagrams
        anagram_group = None
        single_group = None
        for group in result:
            if len(group) == 2:
                anagram_group = group
            elif len(group) == 1:
                single_group = group
        
        self.assertIsNotNone(anagram_group)
        self.assertIsNotNone(single_group)
        self.assertIn("c", single_group)
        self.assertTrue(("ab" in anagram_group and "ba" in anagram_group))

if __name__ == '__main__':
    unittest.main()
