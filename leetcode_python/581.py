# 581. 最短无序连续子数组
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 581.py
@Time : 2022/02/19 23:55:01
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        dup_nums = nums[:]
        dup_nums.sort()
        l = len(nums)
        left, right = 0, 0
        for i in range(l):
            if nums[i] != dup_nums[i]:
                left = i
                break
        for i in range(l - 1, -1, -1):
            if nums[i] != dup_nums[i]:
                right = i
                break
        if left == right:
            return 0
        return right - left + 1
