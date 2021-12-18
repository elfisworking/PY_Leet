# 319. 灯泡开关
# https://leetcode-cn.com/problems/bulb-switcher/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 319.py
@Time : 2021/12/18 15:37:50
@Author : YuMin Zhang
@State : Half-Depedent
@Thinking :
@Tag : Medium
'''
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n + 0.5))
