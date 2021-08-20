def twoArrays(k, A, B):
    # Write your code here
    # Create two arrays (one sorted ascending, one sorted descending):
    A.sort()
    B.sort()
    BPrime = []
    # Create descening array for B:
    for i in range(len(B)):
        BPrime.append(B[len(B)-1-i])
    for i in range(len(A)):
        if(A[i] + BPrime[i] < k):
            return "NO"
    return "YES"
