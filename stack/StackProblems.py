from typing import List


class StackProblems:

    """
    https://neetcode.io/problems/largest-rectangle-in-histogram/question
    You are given an array of integers heights where heights[i] represents the height of a bar.
    The width of each bar is 1.Return the area of the largest rectangle that can be formed among the bars.
    Note: This chart is known as a histogram.
    Example 1: Input: heights = [7,1,7,2,2,4] Output: 8 Example 2:
    Input: heights = [1,3,7] Output: 7
    """
    @staticmethod
    def largestRectangleArea(heights: List[int]) -> int:
        max_area = 0
        stack = []  # Stack stores indices of bars

        # Add sentinel values: 0 at start and end to handle edge cases
        heights = [0] + heights + [0]

        for i in range(len(heights)):
            # When current bar is shorter, calculate areas using taller bars
            while stack and heights[stack[-1]] > heights[i]:
                # Pop the tallest bar and use it as rectangle height
                height_index = stack.pop()
                height = heights[height_index]

                # Width = distance between current position and previous stack top
                width = i - stack[-1] - 1
                area = width * height
                max_area = max(max_area, area)

            stack.append(i)

        return max_area
