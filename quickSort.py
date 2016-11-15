class QuickSort(object):

    def sort(self, arr):
        def quickSort(arr, start, end):
            if start < end:
                idx = partition(arr, start, end)
                if idx > start:
                    quickSort(arr, start, idx - 1)
                if idx < end:
                    quickSort(arr, idx + 1, end)

        def swap(arr, i, j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

        def partition(arr, start, end):
            pivot = arr[end]
            idx = start
            for j in range(start, end):
                if arr[j] <= pivot:
                    swap(arr, idx, j)
                    idx += 1

            swap(arr, idx, end)
            return idx

        quickSort(arr, 0, len(arr) - 1)
        return arr


arr = [1, 3, 2, 4, 5, 7, 1, 2, 100, 9, 20, 19]
print QuickSort().sort(arr)