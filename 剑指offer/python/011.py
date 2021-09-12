# 剑指 Offer II 011. 0 和 1 个数相同的子数组
# https://leetcode-cn.com/problems/A1NYOS/
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [ -1 if i == 0 else i for i in nums]
        sum_value = 0
        res = 0
        d = {}
        d[0] = 0
        for index, i in enumerate(nums):
            sum_value += i
            sub = sum_value 
            if sub in d:
                res = max(res,index-d[sub] + 1)
            if sum_value in d:
                d[sum_value] = min(d[sum_value],index+1)
            else:
                d[sum_value] =index + 1
        return res

