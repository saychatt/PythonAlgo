from random import randint


def findKthSmallest(arr, k):
    if arr is None or len(arr) == 0:
        return 1
    if len(arr) < k:
        return -1
    return findKthSmallestHelper(arr, 0, len(arr) - 1, k)



def findKthSmallestHelper(arr, start, end, k):
    if start == end:
        return arr[start]
    # get a random number between start and end
    random = randint(start, end)
    r = partitionByPivot(arr, start, end, random)

    #rank is same
    if r == k-1:
        return arr[r]
    if k-1 < r:
        return findKthSmallestHelper(arr, start, r - 1, k)
    else:
        return findKthSmallestHelper(arr, r + 1, end, k)


def partitionByPivot(arr, start, end, random):
    #move the pivot element to the end of the array
    arr[random], arr[end] = arr[end], arr[random]
    left = start

    for i in range(start, end):
        if arr[i] < arr[end]:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1

    arr[left], arr[end] = arr[end], arr[left]

    return left
