# 120. 三角形最小路径和
# https://leetcode-cn.com/problems/triangle/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 120.py
@Time : 2021/09/25 14:38:49
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [ [0]*len(triangle[i]) for i in range(m)]
        for i in range(m):
            dp[i][0] = triangle[i][0] + dp[i - 1][0]

        for i in range(1, m):
            l = len(triangle[i])
            for j in range(1,l):
                if j == l-1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        
        return min(dp[m-1])
