def miniMaxSum(arr):
    # Write your code here
    minArr = list(arr)
    maxArr = list(arr)
    minSum = 0
    maxSum = 0
    for iteration in range(4):
        minSum += minArr.pop(minArr.index(min(minArr)))
        maxSum += maxArr.pop(maxArr.index(max(maxArr)))
