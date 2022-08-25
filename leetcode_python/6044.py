# https://leetcode-cn.com/problems/number-of-flowers-in-full-bloom/
# 6044. 花期内花的数目
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 6044.py
@Time : 2022/04/25 00:10:20
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        d = defaultdict(int)
        for begin, end in flowers:
            d[begin] += 1
            d[end + 1] -= 1
        times = sorted(d.keys())
        n = len(persons)
        ans = [0] * n
        i  =  sum = 0
        for p, id in sorted(zip(persons, range(n))):
            while i < len(times) and times[i] <= p:
                sum += d[times[i]]
                i += 1
            ans[id] = sum
        return ans
            