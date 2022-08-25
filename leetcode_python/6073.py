# 6073. 相邻字符不同的最长路径
# https://leetcode-cn.com/problems/longest-path-with-different-adjacent-characters/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 6073.py
@Time : 2022/04/17 22:02:15
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        d = defaultdict(list)
        for i in range(1, len(parent)):
            d[parent[i]].append(i)
        ans = 0
        def dfs(node):
            sec = 0
            fir = 0
            for child in d[node]:
                    depth = dfs(child)
                    if s[child] == s[node]:
                        depth = 0
                    if depth > sec:
                        sec = depth
                    if sec > fir:
                        sec, fir = fir, sec
            nonlocal ans
            ans = max(ans, sec + fir + 1)
            return fir + 1
            
        dfs(0)
        return ans