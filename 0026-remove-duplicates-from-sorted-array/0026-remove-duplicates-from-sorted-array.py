class Solution(object):
    def removeDuplicates(self, nums):
        left = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                nums[left] = nums[i]
                left+=1
        return left

        