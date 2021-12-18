# 672. 灯泡开关 Ⅱ
# https://leetcode-cn.com/problems/bulb-switcher-ii/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 672.py
@Time : 2021/12/18 16:08:48
@Author : YuMin Zhang
@State : Depedent 
@Thinking :
@Tag : Medium
'''
# 超时
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        state = set()
        lamp = 0
        def dfs(lamp, depth):
            if depth == presses:
                state.add(lamp)
                return 
            for i in range(4):
                copy = lamp
                if i == 0:
                    for j in range(0, n, 2):
                        copy ^= 1 << j
                elif i == 1:
                    for j in range(1, n, 2):
                        copy ^= 1 << j
                elif i == 2:
                    for j in range(n):
                        copy ^= 1 << j
                else:
                    j = 0
                    while j < n:
                        copy ^= 1 << j
                        j += 3
                dfs(copy, depth + 1)
        dfs(lamp, 0)
        return len(state)

# 找规律  只与前三个有关系
class Solution(object):
    def flipLights(self, n, m):
        n = min(n, 3)
        if m == 0: return 1
        if m == 1: return [2, 3, 4][n-1]
        if m == 2: return [2, 4, 7][n-1]
        return [2, 4, 8][n-1]
