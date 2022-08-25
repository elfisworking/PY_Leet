# 
# https://leetcode-cn.com/problems/sum-of-scores-of-built-strings/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 2223.py
@Time : 2022/04/19 23:34:11
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def sumScores(self, s: str) -> int:
        MOD = 10**9 + 7
        base = 31
        def encode(ch):
            return ord(ch) - ord('a') + 1
        n = len(s)
        prefix = [0] * (n + 1)
        mul = [1] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = (prefix[i - 1] * base + encode(s[i - 1])) % MOD
            mul[i] = mul[i - 1] * base % MOD
        
        ans = n
        for m in range(1, n):
            if s[n - m] != s[0]:
                continue
            left, right = 0, m + 1
            while left < right:
                mid = left + (right - left) // 2
                hash_val = (prefix[n - m + mid] - prefix[n - m] * mul[mid] % MOD + MOD) %MOD
                if hash_val == prefix[mid]:
                    left = mid + 1
                else:
                    right = mid
            ans += left - 1
        return ans

    # hash_val = ( prefix[n-m+mid] - prefix[n-m] * mul[mid] % MOD + MOD ) % MOD
