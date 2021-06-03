# 740. 删除并获得点数
# https://leetcode-cn.com/problems/delete-and-earn/
from typing import List
class Solution:
    # 艹 怎么想到打家劫舍的  
    # 198 打家劫舍
    #  https://leetcode-cn.com/problems/house-robber/
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxVal = max(nums)
        total = [0]*(maxVal+1)
        for val in nums:
            total[val] += 1
        dp = [0]*(maxVal+1)
        dp[1] = total[1]*1
        dp[2] = max(dp[1],total[2]*2)
        for i in range(2,maxVal+1):
            dp[i] = max(dp[i-1],dp[i-2]+i*total[i])
        return dp[maxVal] 