from timer import timer
from random import randint

@timer
def insertSort(arr):
    '''0(n2)'''
    for i in range(1, len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1]=temp
    return arr



print insertSort([randint(1,10000) for _ in range(1,1000)])
print insertSort([randint(1,10000) for _ in range(1,100)])