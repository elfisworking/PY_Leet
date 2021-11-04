# 367. 有效的完全平方数
# https://leetcode-cn.com/problems/valid-perfect-square/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 367.py
@Time : 2021/11/04 21:09:28
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right =0, num
        while left <= right:
            mid = left + (right - left)//2
            n = mid * mid 
            if n == num:
                return True
            elif n > num:
                right = mid - 1
            else:
                left = mid + 1
        return False