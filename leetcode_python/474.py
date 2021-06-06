# 474. 一和零
# https://leetcode-cn.com/problems/ones-and-zeroes/
from typing import List
class Solution:
    # 深搜会爆
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        Len = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in  range(m + 1)] for _ in range(Len + 1)]
        for k in range(1, Len + 1):
            cnt0 = strs[k-1].count('0')
            cnt1 = strs[k-1].count('1')
            for i in range(m + 1):
                for j in range(n + 1):
                    dp[k][i][j] = dp[k-1][i][j]             #继承
                    if i - cnt0 >= 0 and j - cnt1 >= 0:     #可更新则更新
                        dp[k][i][j] = max(dp[k][i][j], dp[k-1][i-cnt0][j-cnt1] + 1)
            
        return dp[Len][m][n]
