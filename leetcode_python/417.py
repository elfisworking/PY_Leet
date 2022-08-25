# 417. 太平洋大西洋水流问题
# https://leetcode-cn.com/problems/pacific-atlantic-water-flow/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 417.py
@Time : 2022/04/27 10:48:30
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,  n = len(heights), len(heights[0])
        def search(start):
            visited = set()
            def dfs(x, y):
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for nx ,ny in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny)
            for x, y in start:
                dfs(x, y)
            return visited
        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, search(pacific) & search(atlantic)))
        
        