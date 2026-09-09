class Solution(object):
    def twoSum(self, nums, target):
        n = {}
        for i , num in enumerate(nums):
            compliment = target - nums[i]
            if compliment in n:
                return [n[compliment],i]
            n[num] = i
        