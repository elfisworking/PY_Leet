# 1629. 按键持续时间最长的键
# https://leetcode-cn.com/problems/slowest-key/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1629.py
@Time : 2022/01/09 21:46:24
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def slowestKey(self, r: List[int], k: str) -> str:
        d = defaultdict(int)
        d[k[0]] = r[0]
        for i in range(1, len(r)):
            if k[i] not in d:
                d[k[i]] = r[i] - r[i - 1]
            else:
                t = r[i] - r[i -1]
                if t > d[k[i]]:
                    d[k[i]] = t
        d = sorted(d.items(),key = lambda x: (x[1], x[0]), reverse = True)
        return d[0][0]