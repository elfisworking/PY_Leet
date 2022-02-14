# 1984. 学生分数的最小差值
# https://leetcode-cn.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1984.py
@Time : 2022/02/11 22:38:19
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = k - 1
        ans = float("inf")
        l = len(nums)
        while right < l:
            ans = min(ans, nums[right] - nums[left])
            right += 1
            left += 1
        return ans