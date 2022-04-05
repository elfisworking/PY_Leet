# 205. 同构字符串
# https://leetcode-cn.com/problems/isomorphic-strings/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 205.py
@Time : 2022/03/20 21:01:06
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t or len(s) != len(t):
            return False
        d = dict()
        used = set()
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in used:
                    d[s[i]] = t[i]
                    used.add(t[i])
                else:
                    return False
        return True
        