# 739. 每日温度
# https://leetcode-cn.com/problems/daily-temperatures/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 739.py
@Time : 2022/03/19 21:01:46
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        l = len(temperatures)
        ans = [0] * l
        stack = []
        for i in range(l - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            ans[i] = stack[-1][1] - i if stack else 0
            stack.append((temperatures[i], i))
        return ans