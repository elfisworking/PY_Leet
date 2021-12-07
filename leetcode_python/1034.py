#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1034.py
@Time : 2021/12/07 15:19:51
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        pair = []
        h = len(grid)
        b = len(grid[0])
        visited = set()
        def dfs(row, col, fr, fc):
            nonlocal h
            nonlocal b
            flag = False
            visited.add((row,col))
            for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newrow = row + i[0]
                    newcol = col + i[1]
                    if (newrow, newcol) in visited:
                        continue
                    print(newrow, newcol)
                    if  newcol < 0 or newcol >= b or newrow < 0 or newrow >= h:
                        flag = True
                    elif grid[newrow][newcol] != grid[row][col]:
                        flag = True
                    else:
                        dfs(newrow, newcol, row, col)   
            if flag:
                pair.append((row, col))
        
        dfs(row, col, None, None)
        for i in pair:
            grid[i[0]][i[1]] = color
        return grid


s = Solution()
print(s.colorBorder([[1,1,1],[1,1,1],[1,1,1]], 1, 1, 2))