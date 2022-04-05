# 307. 区域和检索 - 数组可修改
# https://leetcode-cn.com/problems/range-sum-query-mutable/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 307.py
@Time : 2022/04/04 20:12:32
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class NumArray:

    def __init__(self, nums: List[int]):
        l = len(nums)
        self.nums = nums
        self.l = l
        self.n = [0] * (l + 1)
        for i in range(0, l):
            self.add(i, nums[i])
        print(self.n)

    def lowbit(self, x):
        return x & (-x)

    def add(self, index, val):
        index += 1
        while index <= self.l :
            self.n[index] += val
            index += self.lowbit(index)

    def update(self, index: int, val: int) -> None:
        self.add(index, val - self.nums[index])
        self.nums[index] = val
        
    def sum(self, i):
        ans = 0
        while i > 0:
            ans += self.n[i]
            i -= self.lowbit(i)
        return ans

    def sumRange(self, left: int, right: int) -> int:
        return self.sum(right + 1) - self.sum(left)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)