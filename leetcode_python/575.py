# 575.分糖果
# https://leetcode-cn.com/problems/distribute-candies/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 575.py
@Time : 2021/11/01 21:23:16
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        l = len(candyType)//2
        counter = Counter(candyType)
        ans = l if l <= len(counter.values()) else len(counter.values())
        return ans