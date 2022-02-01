# 96. 不同的二叉搜索树
# https://leetcode-cn.com/problems/unique-binary-search-trees/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 96.py
@Time : 2022/01/25 19:54:54
@Author : YuMin Zhang
@State : Depedent 
@Thinking :
@Tag : Medium
'''
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]