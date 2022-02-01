#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2146.py
@Time : 2022/01/27 14:21:41
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        d = deque()
        d.append((0, start[0], start[1]))
        row = len(grid)
        col = len(grid[0])
        items = []
        if pricing[0] <= grid[start[0]][start[1]] <= pricing[1]:
            items.append([0, grid[start[0]][start[1]], start[0], start[1]])
        grid[start[0]][start[1]] = 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        while d:
            step, x, y = d.popleft() # 这里写错了 当时写成了pop()
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] > 0:
                    d.append((step + 1, new_x, new_y))
                    if pricing[0] <= grid[new_x][new_y] <= pricing[1]:
                        items.append([step + 1, grid[new_x][new_y], new_x, new_y])
                    grid[new_x][new_y] = 0
        items.sort()
        ans = [item[2:] for item in items][:k]   # 排名最高 k 件物品的坐标
        return ans

