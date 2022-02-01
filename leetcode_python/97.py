# 97. 交错字符串
# https://leetcode-cn.com/problems/interleaving-string/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 97.py
@Time : 2022/01/25 21:20:31
@Author : YuMin Zhang
@State : Depedent 
@Thinking :
@Tag : Medium
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if len(s3) != l1 + l2:
            return False
        dp = [ [False]* (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True
        ptr = 0
        for i in range(0, l1 + 1):
            for j in range(0, l2 + 1):
                ptr = i + j - 1
                if i > 0:
                    dp[i][j] |= dp[i - 1][j] and s1[i - 1] == s3[ptr]
                if j > 0:
                    dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[ptr]
                
        return dp[l1][l2]

