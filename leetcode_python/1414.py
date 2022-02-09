# 1414. 和为 K 的最少斐波那契数字数目
# https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1414.py
@Time : 2022/02/09 16:20:30
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f = [1, 1]
        while f[-1] < k:
            f.append(f[-1] + f[-2])
        ans, i = 0, len(f) - 1
        while k:
            if k >= f[i]:
                k -= f[i]
                ans += 1
            i -= 1
        return ans