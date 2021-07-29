# 剑指 Offer 53 - II. 0～n-1中缺失的数字
# https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 54-II.py
@Time : 2021/07/28 10:48:05
@Author : YuMin Zhang
@State : Nonindepedent | Independent | Half-independent
@Thinking : 
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left , right = 0 ,len(nums)
        while left<right:
            mid  = left + (right-left)//2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid
        return left