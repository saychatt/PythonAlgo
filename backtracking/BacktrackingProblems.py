from typing import List


class BacktrackingProblems:
    """
    https://neetcode.io/problems/subsets/question
    Given an array nums of unique integers, return all possible subsets of nums.
    The solution set must not contain duplicate subsets. You may return the solution in any order.
    Example 1:  Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    Example 2: Input: nums = [7]
    Output: [[],[7]]
    """
    @staticmethod
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # on the tree the left side includes the number
        # on the right side we do not include the number
        currSet, resultSet = [], []

        def helper(i):
            if i >= len(nums):
                # as the currSet will change during recursion
                resultSet.append(currSet.copy())
                return
                # include the next number: left branch
            currSet.append(nums[i])
            helper(i + 1)

            # remove the number
            currSet.pop()
            helper(i + 1)
            # call the helper function which will recurse

        # call the recursive function
        helper(0)
        return resultSet


    """
    https://neetcode.io/problems/search-for-word/question
    Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, 
    otherwise return false. For the word to be present it must be possible to form it with a path in the 
    board with horizontally or vertically neighboring cells. The same cell may not be used more than once
    in a word.
    """
    @staticmethod
    def wordExist(self, board: List[List[str]], word: str) -> bool:
        #find the boundaries
        m, n = len(board), len(board[0])
        #this set is to ensure you are not double including already considered character
        path = set()

        #back tracking function
        def backTrack(i, j, curr):
            #condition is met, word is found
            if curr == len(word):
                return True
            #check areas of failure like boundaries
            if (min(i, j) < 0 or
                    i >= m or
                    j >= n or
                    #if the current character does not match then move on
                    word[curr] != board[i][j] or
                    #if already visited then move on
                    (i, j) in path):
                return False
            #add as this is a valid path to finding the word
            path.add((i, j))

            #you can now move up, down, left or right
            #any of the path is true means the path has been found.
            res = (backTrack(i + 1, j, curr + 1) or
                   backTrack(i - 1, j, curr + 1) or
                   backTrack(i, j + 1, curr + 1) or
                   backTrack(i, j - 1, curr + 1))
            #backtracking formula of removing this cell, or path for the next iteration
            path.remove((i, j))
            return res

        #actual run over the full range of the matrix.
        for i in range(m):
            for j in range(n):
                if backTrack(i, j, 0):
                    return True
        #word did not exist in the matrix
        return False