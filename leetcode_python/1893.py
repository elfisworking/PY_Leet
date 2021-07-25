# 1893. 检查是否区域内所有整数都被覆盖
# https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 1893.py
@Time : 2021/07/25 14:13:33
@Author : YuMin Zhang
'''
## 记得去学习一下差分数组
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        if not ranges:
            return False
        ranges = sorted(ranges,key=lambda x : x[0])
        for i in ranges:
            if i[0] <= left <= i[1]:
                left = i[1] + 1
        return left > right
        # new_ranges = []
        # tmp_range = ranges[0]
        # l = len(ranges)

        # # merge
        # for i in range(1,l):
        #     if tmp_range[0]<=ranges[i][0] <= tmp_range[1]:
        #         tmp_range[1] = max(ranges[i][1],tmp_range[1])
        #     else:
        #         new_ranges.append(tmp_range)
        #         tmp_range = ranges[i]
        
        # for i in new_ranges:
        #     if i[0]<= left and right <= i[1]:
        #         return True
        #     elif i[0] <= left < i[1]:
        #         left = i[1]

        # return False