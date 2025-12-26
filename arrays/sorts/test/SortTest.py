import unittest

from arrays.sorts.HeapSort import minHeapSort
from arrays.sorts.MergeSort import mergeSort
from arrays.sorts.QuickSort import quickSort
from heap.MinHeap import MinHeap


class MyTestCase(unittest.TestCase):
    def testQuickSort(self):
        inputArr = [6,2,4,1,3]
        expectedOutputArr = sorted(inputArr)
        actualOutputArr = quickSort(inputArr)

        self.assertEqual(actualOutputArr, expectedOutputArr)  # add assertion here

    def testMergeSort(self):
        inputArr = [6,2,4,1,3]
        expectedOutputArr = sorted(inputArr)
        actualOutputArr = mergeSort(inputArr)

        self.assertEqual(expectedOutputArr,actualOutputArr)  # add assertion here

    def testHeapSort(self):
        inputArr = [6,2,4,1,3]
        expectedOutputArr = sorted(inputArr)
        actualOutputArr = minHeapSort(inputArr)

        self.assertEqual(expectedOutputArr,actualOutputArr)  # add assertion here

    def testMinHeapify(self):
        inputArr = [6,2,4,1,3]
        expectedOutputArr = [1,3,2,4,6]
        heap = MinHeap()
        actualOutputArr = heap.minHeapifyArray(inputArr)

        self.assertEqual(expectedOutputArr,actualOutputArr)  # add assertion here

if __name__ == '__main__':
    unittest.main()
