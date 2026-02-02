from typing import List


class DynamicPrograms:

    """
    https://neetcode.io/problems/coin-change/question
    You are given an integer array coins representing coins of different
    denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount
    representing a target amount of money.Return the fewest number of coins
    that you need to make up the exact target amount. If it is impossible
    to make up the amount, return -1. You may assume that you have an unlimited number of each coin.
    Example 1: Input: coins = [1,5,10], amount = 12 Output: 3
    Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

    Example 2: Input: coins = [2], amount = 3 Output: -1
    Explanation: The amount of 3 cannot be made up with coins of 2.
    Example 3: Input: coins = [1], amount = 0 Output: 0
    Explanation: Choosing 0 coins is a valid way to make up 0.

    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        return dp[amount] if dp[amount] != (amount + 1) else -1

    """
    Fibonacci
    """

    def fib(self, n):
        if n < 2:
            return n
        #using 2-arrays
        dp, i = [0,1], 2
        while i <= n:
            dp[1], dp[0] = dp[0] + dp[1], dp[1]
            i += 1
        return dp[1]

    #https://neetcode.io/problems/house-robber?list=neetcode150
    #House Robber problem
    def rob(self, nums) -> int:
        # base cases
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        #these values will store the memoizations
        prev1, prev2 = 0, 0
        for value in nums:
            #this is where you add and compare the local max
            prev2, prev1 = max(prev1 + value, prev2), prev2

        return prev2

    #number of unique paths in given matrix to the bottom cell starting from [0,0]
    def uniquePaths(self, rows, cols):
        #note prevRow does not exist at start and is outside/below the last row.
        #the number elements in each row is # of columns.
        prevRow = [0] * cols

        #we start last row, till 0 i.e. <-1, and decrement r by -1
        for r in range(rows - 1, -1, -1):
            #doesn't matter as this will be filled based on the prev row and prev element.
            curRow = [0] * cols
            #the last element is always of value 1 as there is only one way to reach the corner.
            curRow[cols -1] = 1
            #we start at the 2nd column as the first col is 1, till 0, and decrement by -1
            for c in range(cols-2, -1, -1):
                #add the below and right element values. Memoization step.
                curRow[c] = prevRow[c] + curRow[c+1]
            prevRow = curRow
        #final value stored on the top left corner.
        return prevRow[0]

    """
    https://neetcode.io/problems/house-robber-ii/question
    You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
    The houses are arranged in a circle, i.e. the first house and the last house are neighbors.
    You are planning to rob money from the houses, but you cannot rob two adjacent houses because 
    the security system will automatically alert the police if two adjacent houses were both broken into.
    Return the maximum amount of money you can rob without alerting the police.
    Example 1:  Input: nums = [3,4,3]   Output: 4
    Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.
    Example 2:  Input: nums = [2,9,8,3,6]
    Output: 15  Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.
    """

    def circularRob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def simpleRob(houses):
            prev1, prev2 = 0, 0
            for value in houses:
                prev2, prev1 = max(prev2, prev1 + value), prev2
            return prev2
        #run the cases for without the first house, and then without the last house. Take the max of the 2.
        return max(simpleRob(nums[1:]), simpleRob(nums[:-1]))




    #https://neetcode.io/problems/longest-common-subsequence?list=neetcode150
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #initialize the 2D array with 0
        if len(text1)< len(text2):
            text1, text2 = text2, text1
        #keep a track of the values in the 2 arrays
        curr = [0] * (len(text2) + 1)
        prev = [0] * (len(text2) + 1)

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    #add the diagonal element + 1 for matching
                    curr[j] = prev[j+1] + 1
                else:
                    #take the max of side and up arrays
                    curr[j] = max(curr[j+1], prev[j])
            prev, curr = curr, prev

        return prev[0]

    #https://neetcode.io/problems/coin-change-ii/question

