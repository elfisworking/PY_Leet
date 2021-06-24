# 剑指 Offer 10- II. 青蛙跳台阶问题
# https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
class Solution:
    def numWays(self, n: int) -> int:
        # dp[n] = dp[n-1]+dp[n-2]
        if n == 1 or n == 0:
            return 1
        if n == 2:
            return 2
        dp  = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = (dp[i-1]+dp[i-2])%(1000000007)
        return dp[n]
