# 539. 最小时间差
# https://leetcode-cn.com/problems/minimum-time-difference/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 539.py
@Time : 2022/01/18 22:12:51
@Author : YuMin Zhang
@State : Indepeedent 
@Thinking :
@Tag : Medium
'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort(key = lambda x: (x[:2],x[3:]))
        ans = float("inf")
        pre_hour = int(timePoints[0][:2])
        pre_minute = int(timePoints[0][3:])
        for i in range(1, len(timePoints)):
            cur_hour = int(timePoints[i][:2])
            cur_minute = int(timePoints[i][3:])
            sub = (cur_hour - pre_hour) * 60 + cur_minute - pre_minute
            if sub < ans:
                ans = sub
            pre_hour = cur_hour
            pre_minute = cur_minute
        cur_hour = int(timePoints[0][:2])
        cur_minute = int(timePoints[0][3:])
        sub = (24 + cur_hour - pre_hour ) * 60 +  cur_minute - pre_minute
        if sub < ans:
            ans = sub
        return int(ans)