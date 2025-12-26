class DynamicPrograms:

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

        # this array would be used for memoization
        prev = [nums[0], max(nums[0], nums[1])]

        # starting with the 3rd house i.e. index 2
        i = 2
        while i < len(nums):
            # core logic to select if adj house max
            # or skip house max needs to be selected
            prev[1], prev[0] = max(nums[i] + prev[0], prev[1]), prev[1]
            i += 1
        return prev[1]

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

