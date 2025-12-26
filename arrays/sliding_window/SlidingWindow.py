from collections import deque
from typing import List


class SlidingWindow:

   # https://neetcode.io/problems/minimum-window-with-characters
   # Given two strings s and t of lengths m and n respectively,
   # return the minimum window substring of s such that every character
   # in t (including duplicates) is included in the window. If there is no such substring,
   # return the empty string "".
   # The testcases will be generated such that the answer is unique.
   # A substring is a contiguous sequence of characters within the string.
   @staticmethod
   def minCommonSubstring(self, s: str, t: str) -> str:
       if t == "" or s == "":
           return ""
       #map to count of char in the window and needed count
       window, countT = {}, {}
       for c in t:
           countT[c] = 1 + countT.get(c, 0)
       # keeping the overall count of have and actual need. If have == need then valid substring.
       have, need = 0, len(countT)

       #define the results
       result, resultLength = [-1,-1], float("infinity")
       #define the window left and right
       left = 0

       #iterating over the string
       for right in range(len(s)):
           c = s[right]
           window[c] = 1 + window.get(c,0)
           #check if the count of have needs to increase if the count in need matches
           if c in countT and countT[c] == window[c]:
               have += 1
               #if the condition is satisfied have == need
           while have == need:
                if right - left + 1 < resultLength:
                    resultLength = right - left + 1
                    result = [left, right]
                #decrement the left window if an existing character is removed
                window[s[left]] -= 1
                #if existing character is removed decrement the have count
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
       left, right = result
       return s[left:right+1] if resultLength != float("infinity") else ""


   #https://neetcode.io/problems/sliding-window-maximum?list=neetcode150
   #maximum sliding window - Hard
   @staticmethod
   def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       result = []
       # to store the indexes of the elements always in decreasing order.
       q = deque()
       l, r = 0, 0

       while r < len(nums):
           # if the q contains lesser elements pop
           while q and nums[q[-1]] < nums[r]:
               q.pop()
           q.append(r)

           # if the window moves,
           # then remove the previously included element
           if l > q[0]:
               q.popleft()
           # once the window length is reached then
           # start moving the left and also start adding the result.
           if r + 1 >= k:
               result.append(nums[q[0]])
               l += 1
           r += 1
       return result
