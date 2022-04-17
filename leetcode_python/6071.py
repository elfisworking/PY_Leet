# 6071. 完成所有任务需要的最少轮数
# https://leetcode-cn.com/problems/minimum-rounds-to-complete-all-tasks/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 6071.py
@Time : 2022/04/17 22:27:14
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        t = Counter(tasks)
        ans = 0
        for val in t.values():
            a = val // 3
            b = val % 3 
            if b == 1:
                if a < 1:
                    return -1
                a += 1
            elif b == 2:
                a += 1
            ans += a
            
        return ans
                