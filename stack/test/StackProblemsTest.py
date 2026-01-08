import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from StackProblems import StackProblems


class StackProblemsTest(unittest.TestCase):
    def setUp(self):
        self.solution = StackProblems()
    
    def test_example_1(self):
        heights = [7, 1, 7, 2, 2, 4]
        result = self.solution.largestRectangleArea(heights)
        self.assertEqual(result, 8)
    
    def test_example_2(self):
        heights = [1, 3, 7]
        result = self.solution.largestRectangleArea(heights)
        self.assertEqual(result, 7)
    
    def test_single_bar(self):
        heights = [5]
        result = self.solution.largestRectangleArea(heights)
        self.assertEqual(result, 5)
    
    def test_empty_array(self):
        heights = []
        result = self.solution.largestRectangleArea(heights)
        self.assertEqual(result, 0)
    
    def test_increasing_heights(self):
        heights = [1, 2, 3, 4, 5]
        result = self.solution.largestRectangleArea(heights)
        self.assertEqual(result, 9)  # 3 * 3
    
    def test_decreasing_heights(self):
        heights = [5, 4, 3, 2, 1]
        result = self.solution.largestRectangleArea(heights)
        self.assertEqual(result, 9)  # 3 * 3


if __name__ == '__main__':
    unittest.main()
