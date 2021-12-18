#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 419.py
@Time : 2021/12/18 14:01:05
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X":
                    board[i][j] = "."
                    for a in range(i + 1, rows):
                        if board[a][j] == ".":
                            break
                        board[a][j] = "."
                    for a in range(j + 1, cols):
                        if board[i][a] == ".":
                            break
                        board[i][a] = "."
                    ans += 1
        return ans

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        ans = 0
        if board[0][0] == "X":
            ans += 1
        for i in range(1,rows):
            if board[i - 1][0] == "." and board[i][0] == "X":
                ans += 1
        
        for i in range(1, cols):
            if board[0][i - 1] == "." and board[0][i] == "X":
                ans += 1
        
        for i in range(1, rows):
            for j in range(1, cols):
                if board[i - 1][j] == "." and board[i][j - 1] == "." and board[i][j] == "X":
                    ans += 1
        return ans