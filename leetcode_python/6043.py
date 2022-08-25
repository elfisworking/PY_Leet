# 6043. 统计包含每个点的矩形数目
# https://leetcode-cn.com/problems/count-number-of-rectangles-containing-each-point/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 6043.py
@Time : 2022/04/25 20:25:42
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort(key = lambda r : -r[1])
        n = len(points)
        ans = [0] * n
        i, xs = 0, []
        for (x, y), id in sorted(zip(points, range(n)), key=lambda x : -x[0][1]):
            start = i
            while i < len(rectangles) and rectangles[i][1] >= y:
                xs.append(rectangles[i][0])
                i += 1
            if start < i:
                xs.sort()
            ans[id] = i - bisect_left(xs, x)
        return ans