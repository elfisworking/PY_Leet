# 223. 矩形面积
# https://leetcode-cn.com/problems/rectangle-area/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 223.py
@Time : 2021/10/04 14:16:43
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlapWidth = min(ax2, bx2) - max(ax1, bx1)
        overlapHeight = min(ay2, by2) - max(ay1, by1)
        overlapArea = max(overlapWidth, 0) * max(overlapHeight, 0)
        return area1 + area2 - overlapArea
