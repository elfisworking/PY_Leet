# 747. 至少是其他数字两倍的最大数
# https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 747.py
@Time : 2022/01/13 16:38:15
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy
'''
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:return 0
        first, second = nums[0], nums[1]
        ans = 1
        if nums[0] > nums[1]:
            ans = 0
            first, second = second, first
        for i in range(2, len(nums)):
            if nums[i] > second:
                first = second
                second = nums[i]
                ans = i

            elif nums[i] > first:
                first = nums[i]
        print(first, second)
        if first * 2 <= second:
            return ans
        return -1
s = Solution()
print(s.dominantIndex([0,0,0,1]))