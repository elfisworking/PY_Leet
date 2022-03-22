# 152. 乘积最大子数组
# https://leetcode-cn.com/problems/maximum-product-subarray/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 152.py
@Time : 2022/03/22 10:51:09
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [[0]*l for _ in range(2)]
        dp[0][0] = nums[0] # max
        dp[0][1] = nums[0] # min
        for i in range(1, l):
            tmp = [nums[i], nums[i] * dp[0][i - 1], nums[i] * dp[1][i - 1]]
            dp[0][i] = max(tmp)
            dp[1][i] = min(tmp)
        return max(dp[0])
