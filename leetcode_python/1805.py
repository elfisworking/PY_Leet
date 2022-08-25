# 1805. 字符串中不同整数的数目
# https://leetcode-cn.com/problems/number-of-different-integers-in-a-string/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 1805.py
@Time : 2022/04/05 15:02:46
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ""
        for i in word:
            if i.isalpha():
                s += " "
            else:
                s += i
        nums = set(map(int, s.strip().split()))
        return len(nums)