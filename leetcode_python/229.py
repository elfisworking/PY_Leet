# 229. 求众数 II
# https://leetcode-cn.com/problems/majority-element-ii/
from typing import List
from collections import defaultdict
from collections import deque
from collections import Counter
from math import inf
import bisect
import heapq
'''
@File : 229.py
@Time : 2021/10/22 14:50:50
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums) / 3
        counter = Counter(nums)
        ans = []
        for k, v in counter.items():
            if v > l:
                ans.append(k)
        return ans

