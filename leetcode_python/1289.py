# 1289. 下降路径最小和  II
# https://leetcode-cn.com/problems/minimum-falling-path-sum-ii/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1289.py
@Time : 2021/09/25 18:30:23
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
'''
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        l = len(grid)
        dp = [[0]*l for _ in range(2)]
        for i in range(l):
            dp[0][i] = grid[0][i]
        for a in range(1, l):        
            for i in range(l):
                min_value = float("inf")
                for j in range(l):
                    if i != j:
                        min_value = min(min_value,dp[(a - 1) % 2][j])
                dp[a % 2][i] = min_value + grid[a][i]
        return min(dp[(l - 1) % 2])
