from typing import List


class GraphProblems:

    """
    https://neetcode.io/problems/surrounded-regions/question
    You are given a 2-D matrix board containing 'X' and 'O' characters.
    If a continous, four-directionally connected group of 'O's is surrounded by 'X's,
    it is considered to be surrounded. Change all surrounded regions of 'O's to 'X's
    and do so in-place by modifying the input board.
    Input: board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","O","O","X"],
        ["X","X","X","O"]
    ]

    Output: [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","O"]
    ]
    """
    @staticmethod
    def surroundedRegions(self, board: List[List[str]]) -> None:
        rowNum, colNum = len(board), len(board[0])

        def markBorderZeros(r, c):
            if (r < 0 or c < 0 or
                    r == rowNum or c == colNum or
                    board[r][c] != "O"):
                return
                # mark the board
            board[r][c] = "#"
            markBorderZeros(r + 1, c)
            markBorderZeros(r - 1, c)
            markBorderZeros(r, c + 1)
            markBorderZeros(r, c - 1)

        # check all the border Zeros
        for r in range(rowNum):
            if board[r][0] == "O":
                markBorderZeros(r, 0)
            if board[r][colNum - 1] == "O":
                markBorderZeros(r, colNum - 1)

        for c in range(colNum):
            if board[0][c] == "0":
                markBorderZeros(0, c)
            if board[rowNum - 1][c] == "O":
                markBorderZeros(rowNum - 1, c)

        # iterate over all the cells
        for r in range(rowNum):
            for c in range(colNum):
                # if it is X that means it's surrounded
                if board[r][c] == "O":
                    board[r][c] = "X"
                # if it is marked then it's border 0
                elif board[r][c] == "#":
                    board[r][c] = "O"