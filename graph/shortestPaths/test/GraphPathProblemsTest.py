import unittest
import sys
sys.path.append('..')
from GraphPathProblemsTest import GraphPathProblemsTest


class GraphPathProblemsTest(unittest.TestCase):

    def test_all_nodes_reachable(self):
        times = [[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]]
        result = GraphPathProblemsTest.networkDelayTime(None, times, 4, 1)
        self.assertEqual(result, 3)

    def test_not_all_nodes_reachable(self):
        times = [[1, 2, 1], [2, 3, 1]]
        result = GraphPathProblemsTest.networkDelayTime(None, times, 3, 2)
        self.assertEqual(result, -1)

    def test_single_node(self):
        times = []
        result = GraphPathProblemsTest.networkDelayTime(None, times, 1, 1)
        self.assertEqual(result, 0)

    def test_direct_path(self):
        times = [[1, 2, 5]]
        result = GraphPathProblemsTest.networkDelayTime(None, times, 2, 1)
        self.assertEqual(result, 5)

    def test_multiple_paths(self):
        times = [[1, 2, 1], [1, 3, 4], [2, 3, 2]]
        result = GraphPathProblemsTest.networkDelayTime(None, times, 3, 1)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
