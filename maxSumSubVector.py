from timer import timer

@timer
def maxSumSubVector1(arr):
    '''O(n3)'''
    n = len(arr)
    maxSoFar = 0
    for i in range(0, n):
        for j in range(i, n):
            sum = 0
            for v in range(i, j + 1):
                sum += arr[v]
            if(sum > maxSoFar):
                maxSoFar = sum
    return maxSoFar

print maxSumSubVector1([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
