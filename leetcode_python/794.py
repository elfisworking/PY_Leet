# 794. 有效的井字游戏
# https://leetcode-cn.com/problems/valid-tic-tac-toe-state/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 794.py
@Time : 2021/12/09 16:23:29
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        c = [0, 0]
        for i in board:
            for j in i:
                if j == "O":
                    c[0] += 1
                elif j == "X":
                    c[1] += 1
        print(c)
        if c[0] != c[1] and c[0] + 1 != c[1]:
            return False
        def check(ch):
            for i in range(3):
                if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == ch:
                    return True
                if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == ch:
                    return True
            a = False
            if board[1][1] == ch and board[0][0] == ch and board[2][2] == ch:
                a = True
            b = False
            if board[1][1] == ch and board[0][2] == ch and board[2][0] == ch:
                b = True    
            return a or b 
        
        a = check("O")
        b = check("X") 
        if c[0] == c[1] and b:
            return False
        if c[0] + 1 == c[1] and a:
            return False
        if a and b:
            return False
        return True