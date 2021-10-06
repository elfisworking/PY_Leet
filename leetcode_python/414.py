# 414. 第三大的数
# https://leetcode-cn.com/problems/third-maximum-number/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
from sortedcontainers import SortedList
import bisect
import heapq
'''
@File : 414.py
@Time : 2021/10/06 20:03:30
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : max_heaq
'''
class Solution:
    # use sort way
    # def thirdMax(self, nums: List[int]) -> int:
    #     nums = list(set(nums))
    #     nums.sort()
    #     return nums[-3] if len(nums) >=3 else nums[-1]

    # using sorted set
    def thirdMax(self, nums: List[int]) -> int:
        s = SortedList()
        for num in nums:
            if num not in s:
                s.add(num)
                if len(s) > 3:
                    s.pop(3)
        
        return s[0] if len(s) == 3 else s[-1]
