# 661. 图片平滑器
# https://leetcode-cn.com/problems/image-smoother/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 661.py
@Time : 2022/03/21 20:33:02
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        ans = [[0]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < rows and 0 <= nc < cols:
                            ans[r][c] += img[nr][nc]
                            count += 1
                            
                ans[r][c] = ans[r][c]//count

        return ans