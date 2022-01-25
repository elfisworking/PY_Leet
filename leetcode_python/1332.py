# 1332. 删除回文子序列
# https://leetcode-cn.com/problems/remove-palindromic-subsequences/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1332.py
@Time : 2022/01/22 21:05:39
@Author : YuMin Zhang
@State : Indepeedentr
@Thinking :
@Tag : Easy
'''
class Solution:
    # 要么返回1次要么返回2次
    def removePalindromeSub(self, s: str) -> int:
        left , right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return 2
            left += 1
            right -= 1
        return 1
