# 1219. 黄金矿工
# https://leetcode-cn.com/problems/path-with-maximum-gold/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1219.py
@Time : 2022/02/09 17:13:59
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        def dfs(x, y, gold):
            gold += grid[x][y]
            nonlocal ans
            ans = max(ans, gold)

            rec = grid[x][y]
            grid[x][y] = 0
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    dfs(nx, ny, gold)
            grid[x][y] =rec
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, 0)
        return ans
