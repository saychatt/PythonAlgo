def kadaneMaxSum(arr):
    maxSum = arr[0]
    currSum = 0

    for n in arr:
        #this is the non-intuitive part where is the sum becomes 0 then return
        if currSum < 0:
            currSum = 0
        currSum += n
        maxSum = max(maxSum, currSum)

    return maxSum

def kadaneMaxSumSubArray(arr):

    maxSum = arr[0]
    currSum = 0
    maxL, maxR = 0, 0
    L = 0
    for R in range (len(arr)):
        if currSum < 0:
            currSum = 0
            #reset the window
            L = R

        currSum += arr[R]
        if currSum > maxSum:
            maxSum = currSum
            maxL, maxR = L, R

    return [maxL, maxR]