# 剑指 Offer 47. 礼物的最大价值
# https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 47.py
@Time : 2021/07/12 11:04:07
@Author : YuMin Zhang
'''

class Solution:
    # dp
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m , n = len(grid) , len(grid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for a in range(1,m+1):
            for b in range(1,n+1):
                dp[a][b] = grid[a-1][b-1]+max(dp[a-1][b],dp[a][b-1])
        return dp[m][n]