# 498. 对角线遍历
# https://leetcode-cn.com/problems/diagonal-traverse/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 498.py
@Time : 2022/03/08 14:14:09
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        ans = []
        direction = True
        x, y = 0, 0
        while True:
            if direction:
                ans.append(mat[x][y])
                if x == row - 1 and y == col - 1:
                    break
                if y == col - 1:
                    direction = False
                    x += 1
                elif x == 0:
                    direction = False
                    y += 1
                else:
                    x -= 1
                    y += 1
            else:
                ans.append(mat[x][y])
                if x == row - 1 and y == col - 1:
                    break
                if x == row - 1:
                    direction =True
                    y += 1
                elif y == 0:
                    direction = True
                    x += 1
                else:
                    y -= 1
                    x += 1
        return ans

s = Solution()
print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))