# 1005. K 次取反后最大化的数组和
# https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1005.py
@Time : 2021/12/05 17:46:36
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)
        for i in range(k):
            s = heapq.heappop(nums)
            heapq.heappush(nums, -s)
        return sum(nums)