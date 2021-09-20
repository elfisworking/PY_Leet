# # 673. 最长递增子序列的个数
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/
from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 动态规划题
        l = len(nums)
        dp = [1] * l
        counter = [1] * l
        for a in range(1,l):
            tmp = 0
            count = 1
            for b in range(a):
                 if nums[b] < nums[a]:
                    if tmp == dp[b]:
                        count += counter[b]
                    elif tmp < dp[b]:
                        tmp = dp[b]
                        count = counter[b]
            dp[a] += tmp
            counter[a] = count
        print(dp)
        print(counter)
        value = max(dp)
        res = 0
        for i in range(l):
            if dp[i] == value:
                res += counter[i]
        return res