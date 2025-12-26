import unittest
import sys
import os

from backtracking.BacktrackingProblems import BacktrackingProblems

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List

class TestBacktrackingProblems(unittest.TestCase):
    
    def test_empty_array(self):
        result = BacktrackingProblems.subsets(BacktrackingProblems(), [])
        self.assertEqual(result, [[]])
    
    def test_single_element(self):
        result = BacktrackingProblems.subsets(BacktrackingProblems(), [7])
        expected = [[], [7]]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_three_elements(self):
        result = BacktrackingProblems.subsets(BacktrackingProblems(), [1, 2, 3])
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(len(result), 8)
        for subset in expected:
            self.assertIn(subset, result)
    
    def test_two_elements(self):
        result = BacktrackingProblems.subsets(BacktrackingProblems(), [4, 5])
        expected = [[], [4], [5], [4, 5]]
        self.assertEqual(len(result), 4)
        for subset in expected:
            self.assertIn(subset, result)
    
    def test_negative_numbers(self):
        result = BacktrackingProblems.subsets(BacktrackingProblems(), [-1, 0])
        self.assertEqual(len(result), 4)
        self.assertIn([], result)
        self.assertIn([-1], result)
        self.assertIn([0], result)
        self.assertIn([-1, 0], result)

if __name__ == '__main__':
    unittest.main()
