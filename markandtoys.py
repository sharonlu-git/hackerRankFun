def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    numToys = 0
    for i in prices:
        if k-i >= 0:
            numToys += 1
        else:
            break
        k = k-i
    return numToys

