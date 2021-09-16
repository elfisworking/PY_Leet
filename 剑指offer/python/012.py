# 剑指 Offer II 012. 左右两边子数组的和相等
# https://leetcode-cn.com/problems/tvdfij/
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        prefix = 0
        ans = -1
        for i in range(len(nums)):
            if prefix == s - prefix - nums[i]:
                return i
            prefix += nums[i]
        return ans