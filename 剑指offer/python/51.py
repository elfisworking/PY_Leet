from os import lchflags

# 剑指 Offer 51. 数组中的逆序对
# https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 51.py
@Time : 2022/04/01 23:44:53
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        queue = []
        ans = 0
        for i in range(len(nums)):
            loc = bisect.bisect_right(queue, nums[i])
            # print(loc, queue)
            ans += len(queue) - loc
            queue.insert(loc, nums[i])
        return ans