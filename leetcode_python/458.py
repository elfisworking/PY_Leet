# 458. 可怜的小猪
# https://leetcode-cn.com/problems/poor-pigs/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 458.py
@Time : 2021/11/25 10:25:01
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : 信息论 维度
'''
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = 0
        while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs