# 368. 最大整除子集
# https://leetcode-cn.com/problems/largest-divisible-subset/
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1]*len(nums)
        maxSize = 1
        maxVal = dp[0]
        for i in range(len):
            for j in range(i): 
                if nums[i]%nums[j]==0:
                    dp[i] = max(dp[i],dp[j]+1)
                if dp[i] > maxSize:
                    maxSize = dp[i]
                    maxVal = nums[i]
        res = []
        if maxSize == 1:
            res.append(nums[0])
            return res
        for i in range(len-1,-1,-1):
            if dp[i] == maxSize and maxVal % nums[i] == 0:
                res.append(nums[i])
                maxVal = nums[i]
                maxSize -= 1
        return res