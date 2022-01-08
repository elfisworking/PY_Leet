# 871. 最低加油次数
# https://leetcode-cn.com/problems/minimum-number-of-refueling-stops/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 871.py
@Time : 2022/01/08 20:25:39
@Author : YuMin Zhang
@State : Depedent 
@Thinking :
@Tag : Hard
'''
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        res = i = 0
        while startFuel < target:
            while i < len(stations) and stations[i][0] <= startFuel:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq: return -1
            startFuel += -heapq.heappop(pq)
            res += 1
        return res