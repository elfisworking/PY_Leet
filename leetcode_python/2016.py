# 2016. 增量元素之间的最大差值
# https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2016.py
@Time : 2022/02/26 19:54:56
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0] 
        ans = -1
        l = len(nums)
        for i in range(1, l):
            if min_val < nums[i]:
                ans = max(ans, nums[i] - min_val)
            min_val = min(min_val, nums[i])
        return ans