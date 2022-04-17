# LCP 39. 无人机方阵
# https://leetcode-cn.com/problems/0jQkd0/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : lcp39.py
@Time : 2022/04/07 20:05:37
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        n, m = len(source), len(source[0])
        d = defaultdict(int)
        for i in range(n):
            for j in range(m):
                d[source[i][j]] += 1
        
        for i in range(n):
            for j in range(m):
                if target[i][j] in d and d[target[i][j]] > 0:
                    d[target[i][j]] -= 1
        return sum(d.values())