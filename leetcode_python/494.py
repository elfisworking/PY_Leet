# 494. 目标和
# https://leetcode-cn.com/problems/target-sum/
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l  = len(nums)
        dp = [[0 for _ in range(l+1)] for _ in range(l+1)]
