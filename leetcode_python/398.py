# 398. 随机数索引
# https://leetcode-cn.com/problems/random-pick-index/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 398.py
@Time : 2022/04/25 20:02:15
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for i in range(len(nums)):
            self.d[nums[i]].append(i)
            

    def pick(self, target: int) -> int:
        if target in self.d:
            n = len(self.d[target])
            index = random.randint(0, n - 1)
            return self.d[target][index]
        return -1
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)