# 997. 找到小镇的法官
# https://leetcode-cn.com/problems/find-the-town-judge/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 997.py
@Time : 2021/12/19 12:19:38
@Author : YuMin Zhang
@State : Indepeedent 
@Thinking :
@Tag : Easy
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        a = defaultdict(int)
        d = defaultdict(int)
        for i in trust:
            a[i[0]] += 1
            d[i[1]] += 1
        
        for key, value in d.items():
            if value == n - 1 and a[key] == 0:
                return key
        return -1
        