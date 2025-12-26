
def mergeSort(arr):
    return mergeSortInternal(arr, 0, len(arr)-1)

def mergeSortInternal(arr, start, end):
    if  end <= start:
        return arr
    #find the middle index
    middle = (start + end) // 2

    #recurse on the left and right
    mergeSortInternal(arr, start, middle)
    mergeSortInternal(arr, middle + 1, end)
    #merge the sorted
    merge(arr, start, middle, end)
    return arr


## in place merge function
def merge(arr, start, middle, end):
    #copy into left and right arrays
    leftArr = arr[start:middle+1]
    rightArr = arr[middle + 1:end+1]
    i, j = 0, 0
    k = start
    #check the right most values in both arrays and insert the smallest in the final array
    while i < len(leftArr) and j < len(rightArr):
      if leftArr[i] <= rightArr[j]:
          arr[k] = leftArr[i]
          i += 1
      else:
          arr[k] = rightArr[j]
          j += 1
      k += 1
    #remaining to be filled up
    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1
    while  j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1
    return arr
