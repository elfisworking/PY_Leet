# 821. 字符的最短距离
# https://leetcode-cn.com/problems/shortest-distance-to-a-character/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 821.py
@Time : 2022/04/19 22:08:08
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = len(s)
        l_dir = [0] * l
        r_dir = [0] * l
        prev = float("-inf")
        for index, val in enumerate(s):
            if val == c:
                prev = index
            l_dir[index] = prev
        prev = float("inf")
        for i in range(l - 1, -1, -1):
            if s[i] == c:
                prev = i
            r_dir[i] = prev
        ans = [0] * l
        for i in range(l):
            ans[i] = min(abs(i - l_dir[i]), abs(i - r_dir[i]))
        return ans