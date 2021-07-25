# https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array/
# 1877. 数组中最大数对和的最小值
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 1877.py
@Time : 2021/07/25 20:57:14
@Author : YuMin Zhang
@Thinking : 贪心？？
'''
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        l = len(nums)
        mid = l//2
        for i in range(mid):
            ans = max(ans,nums[i]+nums[l-i-1])
        return ans
    
s = Solution()
print(s.minPairSum([3,5,4,2,4,6]))

