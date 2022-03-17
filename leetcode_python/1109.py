# 1109. 航班预订统计
# https://leetcode-cn.com/problems/corporate-flight-bookings/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1109.py
@Time : 2022/03/09 13:28:44
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for a, b, c in bookings:
            ans[a - 1] += c
            if b == n:
                continue
            ans[b] -= c
        for i in range(1, n):
            ans[i] += ans[i - 1]
        return ans