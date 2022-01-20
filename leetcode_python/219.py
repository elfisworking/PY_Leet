# 219. 存在重复元素 II
# https://leetcode-cn.com/problems/contains-duplicate-ii/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 219.py
@Time : 2022/01/19 22:16:25
@Author : YuMin Zhang
@State : Indepeeden
@Thinking : 除了使用滑动窗口还可以使用哈希表
@Tag : Easy
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums: return False
        l = len(nums)
        s = set()
        right = min(k + 1, len(nums))
        for i in range(right):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        left = 0
        while right < len(nums):
            s.remove(nums[left])
            left += 1
            if nums[right] in s:
                return True
            else:
                s.add(nums[right])
            right += 1
        return False

