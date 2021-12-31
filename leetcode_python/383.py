# 383. 赎金信
# https://leetcode-cn.com/problems/ransom-note/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 383.py
@Time : 2021/12/31 14:32:51
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for i in ransomNote:
            if i in counter and counter[i] > 0:
                counter[i] -= 1
            else:
                return False
        return True