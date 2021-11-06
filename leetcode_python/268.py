# 268. 丢失的数字
# https://leetcode-cn.com/problems/missing-number/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 268.py
@Time : 2021/11/06 21:12:14
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
# 煞笔做法
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         l = len(nums)
#         d = [0] * (l + 1)
#         for i in nums:
#             d[i] = 1
#         idx = d.index(0)
#         return idx
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = (len(nums) + 1 ) * len(nums) // 2
        b = sum(nums)
        return a - b