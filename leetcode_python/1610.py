# 1610. 可见点的最大数目
# https://leetcode-cn.com/problems/maximum-number-of-visible-points/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
from math import atan2
from math import pi
import bisect
import heapq
'''
@File : 1610.py
@Time : 2021/12/16 11:52:33
@Author : YuMin Zhang
@State : Depedent
@Thinking : 
@Tag: Hard
'''
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        sameCnt = 0
        polarDegrees = []
        for p in points:
            if p == location:
                sameCnt += 1
            else:
                polarDegrees.append(atan2(p[1] - location[1], p[0] - location[0]))
        polarDegrees.sort()

        n = len(polarDegrees)
        polarDegrees += [deg + 2 * pi for deg in polarDegrees]

        maxCnt = 0
        right = 0
        degree = angle * pi / 180
        for i in range(n):
            while right < n * 2 and polarDegrees[right] <= polarDegrees[i] + degree:
                right += 1
            maxCnt = max(maxCnt, right - i)
        return sameCnt + maxCnt
