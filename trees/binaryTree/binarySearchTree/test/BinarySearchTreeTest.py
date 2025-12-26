import unittest

from trees.binaryTree.binarySearchTree.BinarySearchTree import BinarySearchTree


class MyTestCase(unittest.TestCase):
    def testBinarySearchTreeFunctions(self):

        bst = BinarySearchTree(4)
        for i in [3,6,2,5,7]:
            bst.insert(bst.root, i)

        self.assertEqual(bst.root.value, 4)
        self.assertEqual(bst.findMin(bst.root).value, 2)

        self.assertEqual(bst.findKthSmallest(bst.root, 2).value, 3)
        self.assertEqual(bst.findKthSmallest(bst.root, 3).value, 4)

        bst.remove(bst.root, 4)
        self.assertEqual(bst.root.value, 5)
        self.assertEqual(bst.search(bst.root,5), True)
        self.assertEqual(bst.search(bst.root, 4), False)

    def testBinarySearchBFS(self):

        bst = BinarySearchTree(4)
        for i in [3,6,2,5,7]:
            bst.insert(bst.root, i)
        result = bst.bfs(bst.root)
        self.assertEqual(result[0].pop(), 4)
        self.assertEqual(result[1].pop(), 6)
        self.assertEqual(result[1].pop(), 3)
        self.assertEqual(result[2].pop(), 7)






if __name__ == '__main__':
    unittest.main()
