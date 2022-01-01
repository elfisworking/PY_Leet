# 72. 编辑距离
# https://leetcode-cn.com/problems/edit-distance/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 72.py
@Time : 2022/01/01 16:37:27
@Author : YuMin Zhang
@State : Depedent 
@Thinking : dp
@Tag : Hard
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp
        n = len(word1)
        m = len(word2)

        if n * m == 0:
            return n + m
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, m + 1):
            dp[0][i] = i
        

        for j in range(1, n + 1):
            dp[j][0] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = dp[i - 1][j] + 1
                right = dp[i][j - 1] + 1
                mid = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    mid += 1
                dp[i][j] = min(left, right, mid)
        return dp[n][m]
                    