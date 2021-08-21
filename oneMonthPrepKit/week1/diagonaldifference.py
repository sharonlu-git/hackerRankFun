def diagonalDifference(arr):
    # Write your code here
    startingx = 0
    startingy = 0
    sumdiagonal = 0
    # Get sum of diagonals from left to right
    for r in range(int(len(arr[0]))):
        sumdiagonal += arr[r][r]
        sumdiagonal -= arr[r][len(arr[0])-1-r]
    return abs(sumdiagonal)
