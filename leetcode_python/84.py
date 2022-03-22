# 84. 柱状图中最大的矩形
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 84.py
@Time : 2022/03/18 20:49:13
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack1 = [(-1, -1)]
        l = len(heights)
        width = [[0] * l for _ in range(2)]
        stack2 = [(-1, l)]
        for i in range(l):
            while stack1 and stack1[-1][0] >= heights[i]:
                stack1.pop()
            width[0][i] = stack1[-1][1]
            stack1.append((heights[i], i))
        
        for i in range(l - 1, -1, -1):
            while stack2 and stack2[-1][0] >= heights[i]:
                stack2.pop()
            width[1][i] = stack2[-1][1]
            stack2.append((heights[i], i))
       # print(width)
        ans = 0
        for index in range(l):
            left = width[0][index]
            right = width[1][index]
            height = heights[index]
            # print(height, right - left - 1)
            ans = max(ans , height * (right - left - 1))
        return ans