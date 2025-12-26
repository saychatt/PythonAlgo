import unittest
from typing import List

from arrays.twoPointer.TwoPointerProblems import TwoPointerProblems

class MaxAreProblemTests(unittest.TestCase):
    def test_normal_case(self):
        heights = [1,8,6,2,5,4,8,3,7]
        self.assertEqual(TwoPointerProblems.maxArea(heights), 49)

    def test_ascending_array(self):
        heights = [1,2,3,4,5,6,7,8]
        self.assertEqual(TwoPointerProblems.maxArea(heights), 16)

    def test_descending_array(self):
        heights = [8,7,6,5,4,3,2,1]
        self.assertEqual(TwoPointerProblems.maxArea(heights), 16)

    def test_equal_heights(self):
        heights = [5,5,5,5,5]
        self.assertEqual(TwoPointerProblems.maxArea(heights), 20)

    def test_empty_array(self):
        heights = []
        with self.assertRaises(Exception):
            TwoPointerProblems.maxArea(heights)

    def test_single_element(self):
        heights = [1]
        with self.assertRaises(Exception):
            TwoPointerProblems.maxArea(heights)

    def test_negative_heights(self):
        heights = [-1, -5, -2, -3, -4]
        with self.assertRaises(Exception):
            TwoPointerProblems.maxArea(heights)

    def test_very_large_array(self):
        heights = [1] * 10000
        self.assertEqual(TwoPointerProblems.maxArea(heights), 9999)

    def test_alternating_heights(self):
        heights = [1,5,1,5,1,5,1,5]
        self.assertEqual(TwoPointerProblems.maxArea(heights), 30)

    def test_maximum_possible_height(self):
        heights = [2**31-1, 2**31-1]
        self.assertEqual(TwoPointerProblems.maxArea(heights), 2**31-1)

    def test_mixed_signs(self):
        heights = [-2, 3, -4, 5, -1, 2]
        with self.assertRaises(Exception):
            TwoPointerProblems.maxArea(heights)

    def test_float_conversion_trap(self):
        heights = [2**30, 2**30, 2**30]
        self.assertEqual(TwoPointerProblems.maxArea(heights), 2**30 * 2)

    def test_sparse_array(self):
        heights = [0,0,0,5,0,0,0,4,0,0]
        self.assertEqual(TwoPointerProblems.maxArea(heights), 16)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)