# 733. 图像渲染
# https://leetcode-cn.com/problems/flood-fill/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 733.py
@Time : 2022/03/17 11:01:54
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        point = image[sr][sc]
        if point == newColor:
            return image
        def dfs(row, col, newColor):
            image[row][col] = newColor
            for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                new_row = row + a
                new_col = col + b
                if  0 <= new_row < m and 0 <= new_col < n and image[new_row][new_col] == point:
                    dfs(new_row, new_col, newColor)
        dfs(sr, sc, newColor)
        return image