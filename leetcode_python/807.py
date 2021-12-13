# 807. 保持城市天际线
# https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 807.py
@Time : 2021/12/13 15:36:23
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        a, b = [0]*rows, [0]*rows
        for i in range(rows):
            for j in range(rows):
                a[i] = max(a[i], grid[i][j])
                b[j] = max(b[j], grid[i][j])
        ans = 0
        for i in range(rows):
            for j in range(rows):
                ans += min(a[i],b[j]) - grid[i][j]
        return ans