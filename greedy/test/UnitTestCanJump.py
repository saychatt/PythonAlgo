import unittest
from greedy.GreedyProblems import GreedyProblems


class TestCanJump(unittest.TestCase):
    def test_can_reach_end(self):
        self.assertTrue(GreedyProblems.canJump(None, [1, 2, 0, 1, 0]))

    def test_cannot_reach_end(self):
        self.assertFalse(GreedyProblems.canJump(None, [1, 2, 1, 0, 1]))

    def test_single_element(self):
        self.assertTrue(GreedyProblems.canJump(None, [0]))

    def test_large_jump(self):
        self.assertTrue(GreedyProblems.canJump(None, [5, 0, 0, 0, 0]))

    def test_zero_at_start(self):
        self.assertFalse(GreedyProblems.canJump(None, [0, 1]))


if __name__ == '__main__':
    unittest.main()
