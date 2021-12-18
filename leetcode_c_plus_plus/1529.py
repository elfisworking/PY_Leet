# 1529. 灯泡开关 IV
# https://leetcode-cn.com/problems/bulb-switcher-iv/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1529.py
@Time : 2021/12/18 16:35:24
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        target = "0" + target
        for i in range(1, len(target)):
            if target[i -1] != target[i]:
                ans += 1
        return ans