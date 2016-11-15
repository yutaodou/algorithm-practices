class MergeSort(object):

    def sort(self, arr):
        def mergeSort(arr, start, end):
            if end - start < 2:
                return

            middle = (start + end) / 2
            mergeSort(arr, start, middle)
            mergeSort(arr, middle, end)
            merge(arr, start, middle, end)

        def merge(arr, start, middle, end):
            working = [x for x in arr]

            i = start
            j = middle
            for k in range(start, end):
                if(i < middle and (j >= end or working[i] <= working[j])):
                    arr[k] = working[i]
                    i = i + 1
                else:
                    arr[k] = working[j]
                    j = j + 1

        mergeSort(arr, 0, len(arr))
        return arr



arr = [1, 3, 2, 4, 5, 7, 1, 2, 100, 20, 19]
print MergeSort().sort(arr)
