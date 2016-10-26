#!/usr/bin/env python

class Solution(object):
    def find_in_sub_list(self, target, nums, start):
        for i in range(start, len(nums)):
            if(nums[i] == target):
                return i
        return -1

    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            first = nums[i]
            index = self.find_in_sub_list(target-first, nums, i+1)
            if(index > 0):
                return [i, index]
        return []

solution = Solution()
result = solution.twoSum([2, 7, 11, 15],9)
print result