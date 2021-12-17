# 74. 搜索二维矩阵
# https://leetcode-cn.com/problems/search-a-2d-matrix/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 74.py
@Time : 2021/12/17 15:10:34
@Author : YuMin Zhang
@State : Indepeedent
@Thinking : 二分
@Tag : Medium
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        line = len(matrix)
        row = len(matrix[0])
        left = 0
        right = line * row
        while left < right:
            i, j = divmod((left + right) // 2, row)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                left = i * row + j + 1
            else:
                right = i * row + j
        return False