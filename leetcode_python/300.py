# 最长递增子序列
# https://leetcode-cn.com/problems/longest-increasing-subsequence/
from typing import List
class Solution:
    # 使用动态规划的方法 O(n^2)
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        # dp method
        l = len(nums)
        if l == 1:
            return 1
        dp = [1]*l
        maxlen = 1
        for a in range(1,l):
            tmp = 0
            for b in range(a-1,-1,-1):
                if nums[a] > nums[b]:
                    tmp = max(tmp,dp[b])
            dp[a] += tmp
            maxlen = max(maxlen,dp[a])
                    
        return maxlen

# O(nlogn)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0]*len(nums)
        res = 0
        for num in nums:
            i , j = 0 , res
            while i < j:
                mid = i + (j - i) // 2
                if tails[mid] < num: i = mid + 1
                else: j = mid
            tails[i] = num
            if i == res: res+=1
        return res