from typing import List


class StringOperations:

    """
    Given a string s, find the length of the longest substring without duplicate characters.
    A substring is a contiguous sequence of characters within a string.

    Example 1:  Input: s = "zxyzxyz"    Output: 3
    Explanation: The string "xyz" is the longest without duplicate characters.
    Example 2:  Input: s = "xxxx"   Output: 1
    """
    @staticmethod
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        #keeps the unique chars
        charSet = set()
        #init the left pointer at the first element
        left = 0
        for right in range(len(s)):
            # if the char exists then; keep removing left char from set
            while s[right] in charSet:
                charSet.remove(s[left])
                # increase the left pointer;
                left += 1
            # add the non-repeated character
            charSet.add(s[right])
            # take the max of the previous length or the new length
            result = max(result, right - left + 1)
        return result




    #https://neetcode.io/problems/minimum-remove-to-make-valid-parentheses
    @staticmethod
    def minParanRemoveToMakeValid(self, s:str) -> str:

        # the problem is to ensure we have equal number of open "(" and close ")" i.e. count = 0
        # 1st case if there are more closed ")" then remove the extra ")" i.e. count is -ve
        # 2nd case if there are more open "(" then to maintain the order, remove the extras from last

        res = []
        # extra parenthesis count
        count = 0
        for c in s:
            if c == "(":
                count += 1
                res.append(c)
            elif c == ")" and count > 0:
                count -= 1
                res.append(c)
            # count is 0, then ignore ")" but add non ")"
            elif c != ")":
                res.append(c)
        #now for 2nd case: the result string can contain extra "(" which is count > 0
        # reverse the string
        filtered = []
        for c in res[::-1]:
            if c == "(" and count > 0:
                count -= 1
            else:
                filtered.append(c)
        # reverse the array and convert to single string
        return "".join(filtered[::-1])

    @staticmethod
    def letterCombinations(self, digits: str) -> List[str]:
        dialPad = {2: ["a", "b", "c"],
                   3: ["d", "e", "f"],
                   4: ["g", "h", "i"],
                   5: ["j", "k", "l"],
                   6: ["m", "n", "o"],
                   7: ["p", "q", "r", "s"],
                   8: ["t", "u", "v"],
                   9: ["w", "x", "y", "z"]}

        result = []

        def dfs(i, word):
            print("i: ", i)
            if i == len(digits) and word != "":
                result.append(word)
                return
            charSet = dialPad[int(digits[i])]
            if charSet is not None:
                for char in charSet:
                    word += char
                    dfs(i + 1, word)
                    word = word[:-1]

        if digits is None or digits == "":
            return result
        dfs(0, "")
        return result





