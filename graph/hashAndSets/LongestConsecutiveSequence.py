# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution(object):
    @staticmethod
    def longestConsecutive(nums):

        if not nums:
            return 0
        nums = set(nums)
        maxCount = 0

        for num in nums:
            #this is not the left most
            if num - 1 in nums: continue

            size = 1
            while num + 1 in nums:
                num += 1
                size += 1
            maxCount = max(size, maxCount)
        return maxCount
