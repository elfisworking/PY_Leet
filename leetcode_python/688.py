# 688. 骑士在棋盘上的概率
# https://leetcode-cn.com/problems/knight-probability-in-chessboard/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 688.py
@Time : 2022/02/17 23:14:04
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Medium
'''
## 超出时间限制
class Solution:
    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
        if k == 0:
             return 1.0
        total = 8 ** k
        in_chessboard = 0
        def dfs(row, col, step):
            if 0 <= row < n and 0 <= col < n :
                if step == k:
                    nonlocal in_chessboard
                    in_chessboard += 1
                    return 
                for i , j in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
                    dfs(row + i, col + j, step + 1)
        dfs(row, col, 0)
        return in_chessboard / total

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0] * n for _ in range(n)] for _ in range( k + 1)]
        for step in range(k + 1):
            for i in range(n):
                for j in range(n):
                    if step == 0:
                        dp[step][i][j] = 1
                    else:
                        for di, dj in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                dp[step][i][j] += dp[step - 1][ni][nj] / 8
        return dp[k][row][column] 