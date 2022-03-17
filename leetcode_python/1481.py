# 1481. 不同整数的最少数目
# https://leetcode-cn.com/problems/least-number-of-unique-integers-after-k-removals/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1481.py
@Time : 2022/03/14 16:08:39
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        vals = list(counter.values())
        vals.sort()
        ptr = 0
        l = len(vals)
        while ptr < l:
            if k >= vals[ptr]:
                k -= vals[ptr]
                ptr += 1
            else:
                break
        return l - ptr
