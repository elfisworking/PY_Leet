# 521. 最长特殊序列 Ⅰ
# https://leetcode-cn.com/problems/longest-uncommon-subsequence-i/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 512.py
@Time : 2022/03/05 22:49:51
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return len(a) if len(a) > len(b) else len(b)