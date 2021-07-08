# 剑指 Offer 42. 连续子数组的最大和
# https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 42.py
@Time : 2021/07/08 18:49:33
@Author : YuMin Zhang
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        l = len(nums)
        for i in range(1,l):
            dp.append(max(nums[i],dp[-1] + nums[i]))
        return max(dp)
