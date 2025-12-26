

def quickSort(arr):
    start = 0
    end = len(arr) - 1
    return quickSortRecurse(arr, start, end)


def quickSortRecurse(arr, start, end):
    #basecase
    if end <= start:
        return arr
   #init the pivot
    pivot = arr[end]
    left = start

    # Partition elements smaller than pivot on the left side
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1

    #put the pivot in the either side
    arr[end], arr[left] = arr[left], arr[end]

    #make the recursion call
    quickSortRecurse(arr, start, left-1)
    quickSortRecurse(arr, left+1, end)
    return arr








