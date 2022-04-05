# 315. 计算右侧小于当前元素的个数
# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 315.py
@Time : 2022/04/01 23:10:04
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        queue = []
        res = []
        for i in range(len(nums) - 1, -1, -1):
            loc = bisect.bisect_left(queue, nums[i])
            res.append(loc)
            queue.insert(loc, nums[i])
        return res[::-1]