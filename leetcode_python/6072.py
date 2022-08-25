# 6072. 转角路径的乘积中最多能有几个尾随零
# https://leetcode-cn.com/problems/maximum-trailing-zeros-in-a-cornered-path/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 6072.py
@Time : 2022/04/17 22:26:25
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maxTrailingZeros(self, grid) -> int:
        row = len(grid)
        col = len(grid[0]) 
        prefix_row = [[(0, 0)] * (col + 1) for _ in range(row + 1)]
        prefix_col = [[(0, 0)] * (col  + 1) for _ in range(row + 1)]
        def check(val):
            tmp = val
            two = 0
            five = 0
            while tmp % 5 == 0:
                tmp //= 5
                five += 1
            tmp = val
            while tmp % 2 == 0:
                tmp //= 2
                two += 1
            return (five, two)
        
        for i in range(row):
            for j in range(col):
                two, five = check(grid[i][j])
                prefix_col[i + 1][j + 1] = (prefix_col[i][j + 1][0] + five, prefix_col[i][j + 1][1] + two)
                prefix_row[i + 1][j + 1] = (prefix_row[i + 1][j][0] + five, prefix_row[i + 1][j][1] + two)
        ans = 0           
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                one = min(prefix_row[i][j][0] + prefix_col[i - 1][j][0], prefix_row[i][j][1] + prefix_col[i - 1][j][1])
                two = min(prefix_row[i][-1][0] - prefix_row[i][j - 1][0] + prefix_col[i - 1][j][0], prefix_row[i][-1][1] - prefix_row[i][j - 1][1] + prefix_col[i - 1][j][1])
                three = min(prefix_row[i][j][0] + prefix_col[-1][j][0] - prefix_col[i][j][0], prefix_row[i][j][1] + prefix_col[-1][j][1] - prefix_col[i][j][1])
                four = min(prefix_row[i][-1][0] - prefix_row[i][j - 1][0] + prefix_col[-1][j][0] - prefix_col[i][j][0], prefix_row[i][-1][1] - prefix_row[i][j - 1][1] + prefix_col[-1][j][1] - prefix_col[i][j][1])
                max_val = max([one,two, three, four])
                ans = max(ans, max_val)
        return ans