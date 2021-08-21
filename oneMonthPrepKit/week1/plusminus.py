def plusMinus(arr):
    # Write your code here
    positives = 0.000000
    negatives = 0.000000
    zeros = 0.000000
    for val in arr:
        if val == 0:
            zeros += 1
        elif val > 0:
            positives += 1
        else:
            negatives += 1
    positiveRatio = "{:.6f}".format(positives/len(arr))
    negativeRatio = "{:.6f}".format(negatives/len(arr))
    zeroRatio = "{:.6f}".format(zeros/len(arr))
    print(positiveRatio)
    print(negativeRatio)
    print(zeroRatio)
