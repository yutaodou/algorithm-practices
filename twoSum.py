class Solution(object):

    def twoSum(self, nums, target):
        def find_in_sub_list(target, nums, start):
            for i in range(start, len(nums)):
                if(nums[i] == target):
                    return i
            return -1

        for i in range(0, len(nums)):
            first = nums[i]
            index = find_in_sub_list(target - first, nums, i + 1)
            if(index > 0):
                return [i, index]
        return []

solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 18)
print result
