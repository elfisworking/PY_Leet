# 2170. 使数组变成交替数组的最少操作数
# https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-alternating/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 2170.py
@Time : 2022/04/26 14:29:18
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # start = 0 表示偶数下标，start = 1 表示奇数下标
        # 返回值为最大键，最大键对应的值，次大键，次大键对应的值
        def get(start: int) -> Tuple[int, int, int, int]:
            freq = Counter(nums[start::2])
            best = freq.most_common(2)
            if not best:
                return 0, 0, 0, 0
            if len(best) == 1:
                return *best[0], 0, 0
            
            return *best[0], *best[1]
            
        e1stkey, e1stval, e2ndkey, e2ndval = get(0)
        o1stkey, o1stval, o2ndkey, o2ndval = get(1)

        if e1stkey != o1stkey:
            return n - (e1stval + o1stval)
        
        return n - max(e1stval + o2ndval, o1stval + e2ndval)