# 2172. 数组的最大与和
# https://leetcode-cn.com/problems/maximum-and-sum-of-array/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 2172.py
@Time : 2022/04/26 15:36:24
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        f = [0] * (1 << (2 * numSlots))
        for mask in range(1, len(f)):
            c = bin(mask).count("1")
            if c > len(nums):
                continue
            for i in range(numSlots * 2):
                if mask & (1 << i):
                    f[mask] = max(f[mask], f[mask ^ (1 << i)] + (nums[c - 1] & (i // 2 + 1)))
        return max(f)
        
    