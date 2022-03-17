# 599. 两个列表的最小索引总和
# https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 599.py
@Time : 2022/03/14 14:00:20
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if not list1 or not list2:
            return []
        d = defaultdict(int)
        for index, value in enumerate(list1):
            d[value] = index
        min_index = len(list2) + len(list1)
        ans = []
        for index, value in enumerate(list2):
            if value in d:
                if index + d[value] < min_index:
                    min_index = index + d[value]
                    ans = [value]
                elif index + d[value] == min_index:
                    ans.append(value)
        return ans