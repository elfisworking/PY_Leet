# 600. 不含连续1的非负整数
# https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/
# 抄答案
class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 31
        dp[0] = 1
        dp[1] = 1
        for i in range(2,31):
            dp[i] = dp[i-1] + dp[i-2]

        pre = 0
        res = 0
        for i in range(20,-1,-1):
            val = (1 << i)
            if n & val:
                res += dp[i+1]
                if pre == 1:
                    break
            else:
                pre = 0
            
            if i == 0:
                res += 1
        
        return res