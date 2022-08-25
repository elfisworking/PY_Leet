# 386. Lexicographical Numbers
# https://leetcode-cn.com/problems/lexicographical-numbers/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 386.py
@Time : 2022/04/18 19:52:16
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def recursive(val):
            if val > n:
                return
            add = 10
            if val // 10 == 0:
                add = 9 
            for i in range(val, min(n + 1, val + add)):
                ans.append(i)
                recursive(i * 10)
        recursive(1)
        return ans