# 8. 字符串转换整数 (atoi)
# https://leetcode-cn.com/problems/string-to-integer-atoi/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 8.py
@Time : 2022/01/04 21:35:04
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        i = 0
        flag = True
        if s[0] == "+":
            i += 1
        elif s[0] == "-":
            i += 1
            flag = False
        elif not (ord("0") <= ord(s[0]) <= ord("9")):
            return 0
        
        while i < len(s) and s[i] == "0":
            i += 1
        
        ans = 0
        while i < len(s) and ord("0") <= ord(s[i]) <=ord("9"): 
            ans = ans * 10 + int(s[i])
            ans = min(ans, INT_MAX) if flag else min(ans, -INT_MIN)
            i += 1
        if not flag:
            return -ans
        return ans