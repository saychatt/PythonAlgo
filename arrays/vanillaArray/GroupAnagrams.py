from collections import defaultdict
from typing import List

"""
https://neetcode.io/problems/anagram-groups/question
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
"""
class GroupAnagrams:

    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        #initializes the map to empty list
        resultMap = defaultdict(list)

        for token in strs:
            #take an array of 26 character
            count = [0]*26
            #increase the pocket if the character occurs
            for c in token:
                count [ord(c) - ord('a')] += 1
            # Dictionary keys must be hashable (immutable).
            # Tuples are immutable, so they can be hashed and used as keys. Lists cannot
            resultMap[tuple(count)].append(token)

        return list(resultMap.values())