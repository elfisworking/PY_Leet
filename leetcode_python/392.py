# 392. 判断子序列
# https://leetcode-cn.com/problems/is-subsequence/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 392.py
@Time : 2022/03/20 21:18:06
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if  not s:
            return True
        if s and not t:
            return False
        if not s and not t:
            return True
        ptr = 0
        l = len(s)
        for i in t:
            if i == s[ptr]:
                ptr += 1
                if ptr == l:
                    break
                

        return True if ptr == l else False