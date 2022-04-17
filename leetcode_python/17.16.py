# 面试题 17.16. 按摩师
# https://leetcode-cn.com/problems/the-masseuse-lcci/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 17.16.py
@Time : 2022/04/07 19:38:16
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        for i in range(2, len(nums)):
            max_val = nums[0]
            for j in range(1, i -1):
                max_val = max(max_val, nums[j])
            nums[i] += max_val
        return max(nums)

class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        nums[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])