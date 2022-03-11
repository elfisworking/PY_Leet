# 553. 最优除法
# https://leetcode-cn.com/problems/optimal-division/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 553.py
@Time : 2022/02/27 16:10:59
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        l = len(nums)
        if l == 1:
            return str(nums[0])
        if l == 2:
            return str(nums[0]) + "/" + str(nums[1])
        tmp = ""
        for i in range(2, len(nums)):
            tmp += "/" + str(nums[i])
        return str(nums[0]) + "/(" + str(nums[1]) + tmp + ")"
        
        