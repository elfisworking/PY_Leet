# 剑指 Offer II 069. 山峰数组的顶部
# https://leetcode-cn.com/problems/B1IidL/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2069.py
@Time : 2021/10/14 20:30:02
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : binary search
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid - 1] < arr[mid] < arr[mid + 1]:
                left = mid + 1
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                right = mid - 1
            else:
                return mid
        return left