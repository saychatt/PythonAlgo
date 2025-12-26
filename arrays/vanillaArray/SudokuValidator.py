from typing import List

"""
https://neetcode.io/problems/valid-sudoku/question?list=neetcode150
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

1. Each row must contain the digits 1-9 without duplicates.
2. Each column must contain the digits 1-9 without duplicates.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Does not need to full or be solvable to be valid.

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true

"""
class SudokuValidator:

    @staticmethod
    def isValidSudoku(board: List[List[str]]) -> bool:

        boxMatrix = [[set() for _ in range(3)] for _ in range(3)]
        colMapSet, rowSet = {}, set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                # clear the rowSet at the start of each row
                if j == 0:
                    rowSet = set()

                cellStr = board[i][j]
                if cellStr == ".":
                    continue
                num = int(cellStr)
                # check the range
                if num < 0 or num > 9:
                    return False

                # ROW VALIDATION
                # check duplicate in row
                if num in rowSet:
                    return False
                # not a duplicate add
                rowSet.add(num)

                # COLUMN VALIDATION
                # check for column duplicate
                if j not in colMapSet:
                    colMapSet[j] = set()
                if num in colMapSet[j]:
                    return False
                colMapSet[j].add(num)

                # BOX VALIDATION
                boxSet = boxMatrix[i // 3][j // 3]
                if num in boxSet:
                    return False
                boxSet.add(num)
                boxMatrix[i // 3][j // 3] = boxSet

        return True