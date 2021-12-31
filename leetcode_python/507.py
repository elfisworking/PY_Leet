# https://leetcode-cn.com/problems/perfect-number/
# 507. 完美数
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 507.py
@Time : 2021/12/31 14:07:28
@Author : YuMin Zhang
@State : Indepeedent
@Tag : Easy
'''
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        sq = int(sqrt(num)) + 1
        count = num - 1
        for i in range(2, sq):
            if num % i == 0:
                count -= i
                if (b := num // i) != i:
                    count -= b
            if count < 0:
                return False
        return count == 0
            