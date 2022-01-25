# 139. 单词拆分
# https://leetcode-cn.com/problems/word-break/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 139.py
@Time : 2022/01/25 17:02:33
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        l = len(s)
        dp = [False] * (l + 1)
        dp[0] = True
        for i in range(1, l + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[l]