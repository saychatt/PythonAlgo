import unittest

from arrays.vanillaArray.SudokuValidator import SudokuValidator


class SudokuValidatorTest(unittest.TestCase):
    
    def test_valid_partial_board(self):
        """Test the provided valid example"""
        board = [
            ["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        from arrays.vanillaArray.SudokuValidator import SudokuValidator
        self.assertTrue(SudokuValidator.isValidSudoku(board))

    def test_empty_board(self):
        """Test completely empty board"""
        board = [["." for _ in range(9)] for _ in range(9)]
        self.assertTrue(SudokuValidator.isValidSudoku(board))

    def test_invalid_row_duplicate(self):
        """Test invalid board with duplicate in row"""
        board = [["." for _ in range(9)] for _ in range(9)]
        board[0][0] = "1"
        board[0][1] = "1"
        self.assertFalse(SudokuValidator.isValidSudoku(board))

    def test_invalid_column_duplicate(self):
        """Test invalid board with duplicate in column"""
        board = [["." for _ in range(9)] for _ in range(9)]
        board[0][0] = "2"
        board[1][0] = "2"
        self.assertFalse(SudokuValidator.isValidSudoku(board))

    def test_invalid_box_duplicate(self):
        """Test invalid board with duplicate in 3x3 box"""
        board = [["." for _ in range(9)] for _ in range(9)]
        board[0][0] = "3"
        board[1][1] = "3"
        self.assertFalse(SudokuValidator.isValidSudoku(board))

    def test_valid_complete_board(self):
        """Test valid complete Sudoku"""
        board = [
            ["5","3","4","6","7","8","9","1","2"],
            ["6","7","2","1","9","5","3","4","8"],
            ["1","9","8","3","4","2","5","6","7"],
            ["8","5","9","7","6","1","4","2","3"],
            ["4","2","6","8","5","3","7","9","1"],
            ["7","1","3","9","2","4","8","5","6"],
            ["9","6","1","5","3","7","2","8","4"],
            ["2","8","7","4","1","9","6","3","5"],
            ["3","4","5","2","8","6","1","7","9"]
        ]
        self.assertTrue(SudokuValidator.isValidSudoku(board))

    def test_single_number_valid(self):
        """Test board with single number"""
        board = [["." for _ in range(9)] for _ in range(9)]
        board[4][4] = "5"
        self.assertTrue(SudokuValidator.isValidSudoku(board))

    def test_edge_case_box_boundaries(self):
        """Test numbers at box boundaries"""
        board = [["." for _ in range(9)] for _ in range(9)]
        board[2][2] = "1"  # Bottom-right of top-left box
        board[3][3] = "1"  # Top-left of center box
        self.assertTrue(SudokuValidator.isValidSudoku(board))

if __name__ == '__main__':
    unittest.main()
