# 剑指 Offer 10- I. 斐波那契数列
# https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = (dp[i-1]+dp[i-2])%(10**9+7)
        return dp[n]
        