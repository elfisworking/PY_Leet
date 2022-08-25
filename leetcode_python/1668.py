# 1668. 最大重复子字符串
# https://leetcode-cn.com/problems/maximum-repeating-substring/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 1668.py
@Time : 2022/04/05 15:01:55
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        s_l = len(sequence)
        w_l = len(word)
        if w_l > s_l:
            return 0
        ans = 0
        s = word
        while sequence.find(s) != -1:
            ans += 1
            s += word

        return ans

