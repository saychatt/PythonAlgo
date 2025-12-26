import unittest

from arrays.kadane.KadaneMaxSum import kadaneMaxSum, kadaneMaxSumSubArray


class TestKadaneMaxSumSubArray(unittest.TestCase):
    def test_kadane_largest_sum(self):
        arr = [4,-1,2,-7,3,4]
        self.assertEqual(kadaneMaxSum(arr), 7)  # add assertion here

    def test_kadane_largest_sum_subarray(self):
        arr = [4,-1,2,-7,3,4]
        subArr = kadaneMaxSumSubArray(arr)
        self.assertEqual(subArr, [4,5])


if __name__ == '__main__':
    unittest.main()
