# 69. Sqrt(x)
# https://leetcode-cn.com/problems/sqrtx/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 69.py
@Time : 2022/01/16 14:02:33
@Author : YuMin Zhang
@State : Indepeedent 
@Thinking : binary search
@Tag : Easy
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        left , right = 0, x
        while left < right:
            mid = left + (right - left) // 2
            if mid and mid >= (x / mid):
                right = mid
            else:
                left = mid + 1
        if right == x / right: return right
        return right - 1