#!/usr/bin/env python


class QuickSort(object):

    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)
        return arr

    def quickSort(self, arr, start, end):
        if start < end:
            idx = self.partition(arr, start, end)

            if idx > start:
                self.quickSort(arr, start, idx - 1)
            if idx < end:
                self.quickSort(arr, idx + 1, end)

    def partition(self, arr, start, end):
        pivot = arr[end]
        idx = start

        for j in range(start, end):
            if arr[j] <= pivot:
                tmp = arr[idx]
                arr[idx] = arr[j]
                arr[j] = tmp
                idx += 1

        arr[end] = arr[idx]
        arr[idx] = pivot

        return idx

arr = [1, 3, 2, 4, 5, 7, 1, 2, 100, 9, 20, 19]
print QuickSort().sort(arr)
