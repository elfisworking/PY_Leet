# 73. 矩阵置零
# https://leetcode-cn.com/problems/set-matrix-zeroes/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : offer73.py
@Time : 2021/12/16 21:39:29
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m , n  = len(matrix), len(matrix[0])
        flag_col0 = any(matrix[i][0] == 0 for j in range(m))
        flag_row0 = any(matrix[0][i] == 0 for j in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] ==0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0

        if flag_row0:
            for i in range(n):
                matrix[0][j] = 0