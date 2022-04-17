# 796. 旋转字符串
# https://leetcode-cn.com/problems/rotate-string/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 796.py
@Time : 2022/04/07 10:18:28
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        for i in range(1, len(s)):
            a = s[:i]
            b = s[i:]
            c = b + a
            if c == goal:
                return True
        return False
        