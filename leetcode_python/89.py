# 89. 格雷编码
# https://leetcode-cn.com/problems/gray-code/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 89.py
@Time : 2021/12/21 19:42:26
@Author : YuMin Zhang
@State :Half-Depedent 
@Thinking :
@Tag :Medium
'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res
