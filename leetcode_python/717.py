# 717. 1比特与2比特字符
# https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 717.py
@Time : 2022/02/20 22:05:28
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] == 1:
            return False
        idx = 0
        l = len(bits)
        step = 0
        while idx < l:
            if bits[idx] == 1:
                step = 2
                idx += 2
            else:
                step = 1
                idx += 1
        if step == 1:
            return True
        return False