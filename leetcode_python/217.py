# 217. 存在重复元素
# https://leetcode-cn.com/problems/contains-duplicate/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 217.py
@Time : 2022/03/19 21:00:02
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return True
        return False