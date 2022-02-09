# 1725. 可以形成最大正方形的矩形数目
# https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1725.py
@Time : 2022/02/09 17:04:52
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        d = defaultdict(int)
        max_value = 0
        for i in rectangles:
            min_value = min(i[0], i[1])
            max_value = max(max_value, min_value)
            d[min_value] += 1
        return d[max_value]