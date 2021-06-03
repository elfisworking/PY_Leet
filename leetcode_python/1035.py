# 1035. 不相交的线
# https://leetcode-cn.com/problems/uncrossed-lines/
# 是 1143 最长公共子序列的变体
from typing import List
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1 , l2  = len(nums1),len(nums2)
        dp = [ [0 for _ in range(l2+1)] for _ in range(l1+1)]
        for a in range(1,l1+1):
            for b in range(1,l2+1):
                if nums1[a-1] == nums2[b-1]:
                    dp[a][b] = dp[a-1][b-1] + 1
                else:
                    dp[a][b] = max(dp[a-1][b],dp[a][b-1])
        return dp[l1][l2]
            
