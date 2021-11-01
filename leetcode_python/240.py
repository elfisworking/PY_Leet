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

# 2021.10.25
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         a, b = len(matrix), len(matrix[0])
#         for i in range(a):
#             if target > matrix[i][-1]:
#                 continue
#             else:
#                 left, right = 0, b - 1
#                 while left <= right:
#                     mid = left + (right - left) // 2
#                     if matrix[i][mid] == target:
#                         return True
#                     elif matrix[i][mid] > target:
#                         right = mid - 1
#                     else:
#                         left = mid + 1
#         return False

        
