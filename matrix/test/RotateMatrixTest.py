import unittest

from matrix.RotateMatrix import RotateMatrix

class TestRotateMatrix(unittest.TestCase):
    
    def test_2x2_matrix(self):
        matrix = [[1, 2], [3, 4]]
        RotateMatrix.rotateMatrix(None, matrix)
        expected = [[3, 1], [4, 2]]
        self.assertEqual(matrix, expected)
    
    def test_3x3_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        RotateMatrix.rotateMatrix(None, matrix)
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(matrix, expected)
    
    def test_4x4_matrix(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        RotateMatrix.rotateMatrix(None, matrix)
        expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        self.assertEqual(matrix, expected)
    
    def test_1x1_matrix(self):
        matrix = [[1]]
        RotateMatrix.rotateMatrix(None, matrix)
        expected = [[1]]
        self.assertEqual(matrix, expected)