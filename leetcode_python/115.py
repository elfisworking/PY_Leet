# 115. 不同的子序列
# https://leetcode-cn.com/problems/distinct-subsequences/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 115.py
@Time : 2022/03/22 11:24:46
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sl = len(s)
        tl = len(t)
        dp = [[0] * (sl + 1) for _ in range(tl + 1)]
        for i in range(sl + 1):
            dp[0][i] = 1
        for i in range(1, tl + 1):
            for j in range(1, sl + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[tl][sl]