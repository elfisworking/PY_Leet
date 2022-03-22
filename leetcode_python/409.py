# 409. 最长回文串
# https://leetcode-cn.com/problems/longest-palindrome/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 409.py
@Time : 2022/03/16 22:19:59
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        odd = False
        for val in counter.values():
            if val % 2 == 0:
                ans += val
            else:
                ans += val - 1
                odd = True
        if odd:
            ans += 1
        return ans