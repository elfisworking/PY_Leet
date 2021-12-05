# 1446. 连续字符
# https://leetcode-cn.com/problems/consecutive-characters/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1446.py
@Time : 2021/12/01 14:22:24
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def maxPower(self, s: str) -> int:
        l, r = 0 , 0
        max_l = 1
        while r < len(s):
            if s[l] == s[r]:
                max_l = max(max_l, r - l + 1)
                r += 1
            else:
                l = r
        return max_l