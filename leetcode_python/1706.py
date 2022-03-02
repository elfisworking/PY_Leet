# 1706. 球会落何处
# https://leetcode-cn.com/problems/where-will-the-ball-fall/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1706.py
@Time : 2022/02/24 23:26:05
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row = len(grid)
        col = len(grid[0])
        def check(n):
            for i in range(row):
                if n < col - 1 and grid[i][n] == 1 and grid[i][n + 1] == 1:
                    n = n + 1
                elif n > 0 and grid[i][n] == -1 and grid[i][n - 1] == -1:
                    n = n - 1
                else:
                    return (False, - 1)
            return (True, n)
        ans = []
        for i in range(col):
            flag, n  = check(i)
            ans.append(n)
        return ans
 