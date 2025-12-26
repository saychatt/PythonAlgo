import unittest
import sys
sys.path.append('..')
from DijkstraWeightedShortestPath import DijkstraWeightedShortestPath


class DijkstraWeightedShortestPathTests(unittest.TestCase):

    def test_basic_path(self):
        edges = [[1, 2, 1], [2, 3, 1], [1, 3, 3]]
        result = DijkstraWeightedShortestPath.shortestPath(edges, 3, 1)
        self.assertEqual(result, {1: 0, 2: 1, 3: 2})

    def test_single_node(self):
        edges = []
        result = DijkstraWeightedShortestPath.shortestPath(edges, 1, 1)
        self.assertEqual(result, {1: 0})

    def test_disconnected_graph(self):
        edges = [[1, 2, 1]]
        result = DijkstraWeightedShortestPath.shortestPath(edges, 3, 1)
        self.assertEqual(result, {1: 0, 2: 1})

    def test_multiple_paths(self):
        edges = [[1, 2, 4], [1, 3, 2], [3, 2, 1], [2, 4, 1], [3, 4, 5]]
        result = DijkstraWeightedShortestPath.shortestPath(edges, 4, 1)
        self.assertEqual(result, {1: 0, 3: 2, 2: 3, 4: 4})

    def test_weighted_edges(self):
        edges = [[1, 2, 10], [1, 3, 5], [3, 2, 2]]
        result = DijkstraWeightedShortestPath.shortestPath(edges, 3, 1)
        self.assertEqual(result, {1: 0, 3: 5, 2: 7})


if __name__ == '__main__':
    unittest.main()
