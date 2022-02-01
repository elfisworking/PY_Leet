# 1763. 最长的美好子字符串
# https://leetcode-cn.com/problems/longest-nice-substring/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1763.py
@Time : 2022/02/01 21:12:07
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        l = len(s)
        max_pos, max_len = 0, 0
        for i in range(l):
            lower = 0
            upper = 0
            for j in range(i, l):
                if s[j].islower():
                    lower |= 1 << (ord(s[j]) - ord("a"))
                else:
                    upper |= 1 << (ord(s[j]) - ord("A"))
                if lower == upper and j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_pos = i
        return s[max_pos: max_pos + max_len]