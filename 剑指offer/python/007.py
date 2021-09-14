# 剑指 Offer II 007. 数组中和为 0 的三个数
# https://leetcode-cn.com/problems/1fGaJU/
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l < 3:
            return []
        nums.sort()
        res = []
        for i in range(l-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            if nums[i] > 0:
                return res
            left , right = i+1, l-1
            while left < right:
                sum_value = nums[i] + nums[left] + nums[right]
                if sum_value > 0:
                    right -= 1
                elif sum_value < 0:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    right -= 1
        return res