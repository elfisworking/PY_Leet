# 1646. 获取生成数组中的最大值
# https://leetcode-cn.com/problems/get-maximum-in-generated-array/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1646.py
@Time : 2022/03/22 10:35:32
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        ans = 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            prev = i // 2
            mod = i % 2
            if mod == 0:
                c = dp[prev]
            else:
                c = dp[prev] + dp[prev + 1]
            dp[i] = c
            ans = max(ans ,c)
        return ans
                