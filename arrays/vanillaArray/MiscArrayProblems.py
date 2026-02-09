from typing import List


class MiscArrayProblems:


    """
    Given an integer array nums, return an array output
    where output[i] is the product of all the elements of nums
    except nums[i].Each product is guaranteed to fit in a 32-bit integer.
    Follow-up: Could you solve it in  O(n) time without using the division operation?
    Example 1: Input: nums = [1,2,4,6] Output: [48,24,12,8]
    Example 2: Input: nums = [-1,0,1,2,3] Output: [0,-6,0,0,0]
    """
    @staticmethod
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output[i] = product[left] * product[right]
        output = [0] * len(nums)

        prefix = 1
        # iterate from left to right
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        # iterate from the right to left
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output