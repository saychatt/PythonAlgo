from heap.MinHeap import MinHeap


def minHeapSort(arr):

    minHeap = MinHeap()
    for num in arr:
        minHeap.push(num)
    for i in range(0,len(arr)):
        arr[i] = minHeap.pop()

    return arr