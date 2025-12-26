import unittest

from trees.binaryTree.binaryTree.BTNode import BTNode
from trees.binaryTree.binaryTree.BinaryTree import BinaryTree


class MyTestCase(unittest.TestCase):
    def test_something(self):
        bt = BinaryTree()
        btRoot = BTNode(5)

        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
