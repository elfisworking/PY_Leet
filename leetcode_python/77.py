# 77. 组合
# https://leetcode-cn.com/problems/combinations/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 77.py
@Time : 2021/12/17 15:29:41
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(begin, p, d):
            if k == d:
                ans.append(p[:])
            for i in range(begin, n + 1):
                p.append(i)
                dfs(i + 1, p, d+1)
                p.pop()
    
        dfs(1, [], 0)
        return ans

        