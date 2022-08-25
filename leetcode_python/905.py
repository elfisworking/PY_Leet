# 905. 按奇偶排序数组
# https://leetcode-cn.com/problems/sort-array-by-parity/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 905.py
@Time : 2022/04/28 23:03:32
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = -1, 0
        n = len(nums)
        while right < n:
            if nums[right] % 2 == 0:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
            right += 1
        return nums