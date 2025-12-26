from typing import List


class TwoPointerProblems:

    """
    https://neetcode.io/problems/max-water-container/question
    You are given an integer array heights where heights[i] represents the height of the i th bar.
    You may choose any two bars to form a container. Return the maximum amount of water a container can store.
    """
    @staticmethod
    def maxArea(heights: List[int]) -> int:
        if len(heights) < 2:
            raise ValueError("Array must contain at least 2 elements")
        # Check for negative heights
        if any(h < 0 for h in heights):
            raise ValueError("Heights cannot be negative for a water container")

        p1, p2 = 0, len(heights) - 1
        maxVol = float("-inf")

        while p1 < p2:
            l = p2 - p1
            h = min(heights[p1], heights[p2])
            vol = l*h
            maxVol = max(vol, maxVol)
            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1
        return maxVol

    """ HARD 
    https://neetcode.io/problems/trapping-rain-water/question
    You are given an array of non-negative integers height which represent an elevation map. 
    Each value height[i] represents the height of a bar, which has a width of 1.
    Return the maximum area of water that can be trapped between the bars.
    
    Input: height = [0,2,0,3,1,0,1,3,2,1] Output: 9
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] Output: 6
    Input: height = [4,2,3] Output: 1
    """
    @staticmethod
    def trap(height: List[int]) -> int:
        # for each cell : height [i] how much water can be trapped can be found out by
        # find the max height of the right
        # find the min height of the left
        # take the min of the above : Say Min
        # Subtract current value from Min i.e. Min - height[i] - this is non-intuitive
        # Using 2 pointers you keep updating the max left and right and move the pointer whichever is lower.
        if len(height) < 2:
            return 0

        l, r = 0, len(height) - 1
        trap = 0
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                trap += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                trap += maxR - height[r]

        return trap