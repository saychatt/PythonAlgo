import unittest

from arrays.twoPointer.TwoPointerProblems import TwoPointerProblems


class TestTrap(unittest.TestCase):
    
    def test_given_examples(self):
        self.assertEqual(TwoPointerProblems.trap([0,2,0,3,1,0,1,3,2,1]), 9)
        self.assertEqual(TwoPointerProblems.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
        self.assertEqual(TwoPointerProblems.trap([4,2,3]), 1)
    
    def test_edge_cases(self):
        self.assertEqual(TwoPointerProblems.trap([]), 0)
        self.assertEqual(TwoPointerProblems.trap([1]), 0)
        self.assertEqual(TwoPointerProblems.trap([1,1]), 0)
    
    def test_no_water_trapped(self):
        self.assertEqual(TwoPointerProblems.trap([1,2,3,4,5]), 0)
        self.assertEqual(TwoPointerProblems.trap([5,4,3,2,1]), 0)
        self.assertEqual(TwoPointerProblems.trap([3,3,3,3]), 0)
    
    def test_simple_cases(self):
        self.assertEqual(TwoPointerProblems.trap([3,0,2]), 2)
        self.assertEqual(TwoPointerProblems.trap([2,0,2]), 2)
        self.assertEqual(TwoPointerProblems.trap([3,2,0,4]), 4)

if __name__ == '__main__':
    unittest.main()
