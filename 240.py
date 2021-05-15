# 240. 搜索二维矩阵 II
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        x , y = 0 , cols-1
        while x < rows and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1

        return False

        
