# 334. 递增的三元子序列
# https://leetcode-cn.com/problems/increasing-triplet-subsequence/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 334.py
@Time : 2022/01/12 20:18:37
@Author : YuMin Zhang
@State : Depedent 
@Thinking :
@Tag : Medium
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = len(nums)
        if l < 3: return False
        first, second = nums[0] , inf
        for i in range(1, l):
            num = nums[i]
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False