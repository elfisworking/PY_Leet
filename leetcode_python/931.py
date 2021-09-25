# 931. 下降路径最小和
# https://leetcode-cn.com/problems/minimum-falling-path-sum/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 931.py
@Time : 2021/09/25 18:08:19
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
'''
class Solution(object):
    def minFallingPathSum(self, A):
        while len(A) >= 2:
            row = A.pop()            
            for i in range(len(row)):
                A[-1][i] += min(row[max(0,i-1): min(len(row), i+2)])
        return min(A[0])
