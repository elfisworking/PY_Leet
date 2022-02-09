# 2006. 差的绝对值为 K 的数对数目
# https://leetcode-cn.com/problems/count-number-of-pairs-with-absolute-difference-k/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2006.py
@Time : 2022/02/09 16:15:13
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        d = defaultdict(int)
        ans = 0
        for i in nums:
            j = i - k
            if j in d:
                ans += d[j]
            d[i] += 1
        return ans