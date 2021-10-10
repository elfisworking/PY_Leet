# 441. 排列硬币
# https://leetcode-cn.com/problems/arranging-coins/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 441.py
@Time : 2021/10/10 17:54:37
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : simulation or binary search or mathematics
'''
class Solution:
    # one solution 20.2% simulation
    # def arrangeCoins(self, n: int) -> int:
    #     line = 1
    #     ans = 0
    #     while n >= line:
    #         n = n - line
    #         line += 1
    #         ans += 1
    #     return ans
    # one solution binary search
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        def sum_value(mid):
            return (1 + mid) * mid / 2
        while left < right:
            mid = left + (right - left) // 2
            if sum_value(mid) > n:
                right = mid
            else:
                left = mid + 1
        return left - 1 if sum_value(left) > n else left
    # mathematics
    def arrangeCoins(self, n: int) -> int:
        return int((pow(8 * n + 1, 0.5) - 1) / 2)