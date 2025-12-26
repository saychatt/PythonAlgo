import unittest

from arrays.sorts.variations.KthSmallestElement import findKthSmallest


class MyTestCase(unittest.TestCase):
    def test_kthSmallest(self):
        arr = [6, 10, 13, 5, 8, 3, 2, 11]
             # 2, 3, 5, 6, 8, 10, 11, 13
        #Rank  1, 2, 3, 4, 5, 6, 7, 8
        self.assertEqual(2, findKthSmallest(arr, 1))
        self.assertEqual(11, findKthSmallest(arr, 7))
        self.assertEqual(3, findKthSmallest(arr, 2))
        self.assertEqual(6, findKthSmallest(arr, 4))

if __name__ == '__main__':
    unittest.main()
