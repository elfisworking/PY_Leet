# 455. 分发饼干
# https://leetcode-cn.com/problems/assign-cookies/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 455.py
@Time : 2022/03/24 22:16:13
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        ans = 0
        g.sort()
        s.sort()
        g_len = len(g)
        s_len = len(s)
        g_ptr, s_ptr = 0, 0
        while g_ptr < g_len and s_ptr < s_len:
            if g[g_ptr] <= s[s_ptr]:
                ans += 1
                g_ptr += 1
                s_ptr += 1
            else:
                s_ptr += 1
        return ans
