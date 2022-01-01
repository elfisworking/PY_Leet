# 2022. 将一维数组转变成二维数组
# https://leetcode-cn.com/problems/convert-1d-array-into-2d-array/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2022.py
@Time : 2022/01/01 12:34:53
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
'''
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if len(original) != m * n : return []
        tmp = []
        for i in range(1, len(original) + 1):
            tmp.append(original[i - 1])
            if i % n == 0:
                ans.append(tmp)
                tmp = []
        return ans