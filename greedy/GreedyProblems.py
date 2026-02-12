from typing import List


class GreedyProblems:


    """
    https://neetcode.io/problems/jump-game/question
    You are given an integer array nums where each element nums[i]
    indicates your maximum jump length at that position.
    Return true if you can reach the last index starting from index 0, or false otherwise.
    Example 1:  Input: nums = [1,2,0,1,0]   Output: true
    Explanation: First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.
    Example 2:  Input: nums = [1,2,1,0,1]   Output: false
    """
    @staticmethod
    def canJump(self, nums: List[int]) -> bool:
        # this is greedy method; start from the last
        # and check if from the previous element jump can be made
        target = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            # from the previous element jump can be made
            if i + nums[i] >= target:
                # if it can be made then shift the target to left
                target = i
        return True if target == 0 else False