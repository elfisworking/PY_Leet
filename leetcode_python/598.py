# 598. 范围求和 II
# https://leetcode-cn.com/problems/range-addition-ii/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 598.py
@Time : 2021/11/07 14:39:48
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a  = m
        b = n
        for i in ops:
            a = min(a, i[0])
            b = min(b, i[1])
        return a * b 