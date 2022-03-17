# 2055. 蜡烛之间的盘子
# https://leetcode-cn.com/problems/plates-between-candles/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2055.py
@Time : 2022/03/08 14:54:22
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        preSum = [0] * n
        sumValue= 0
        for i in range(n):
            if s[i] == "*":
                sumValue += 1
            preSum[i] = sumValue
        left = [0] * n
        l = -1
        for i in range(n):
            if s[i] == "|":
                l = i
            left[i] = l
        right = [0] * n
        r = -1
        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                r = i
            right[i] = r
        ans = []
        for a, b in queries:
            x = right[a]
            y = left[b]
            if x == -1 or y == -1 or x >= y:
                ans.append(0)
            else:
                ans.append(preSum[y] - preSum[x])
        return ans