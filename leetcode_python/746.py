# 746. 使用最小花费爬楼梯
# https://leetcode-cn.com/problems/min-cost-climbing-stairs/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 746.py
@Time : 2022/03/22 10:26:49
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        if l <= 1:
            return 0
        a = 0 # dp[i - 2]
        b = 0 # dp[i - 1]
        c = None
        for i in range(2, l + 1):
            c = min(a + cost[i - 2], b + cost[i - 1])
            a, b = b , c
        return c