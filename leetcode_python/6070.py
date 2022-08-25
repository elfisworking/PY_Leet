# 6070. 计算字符串的数字和
# https://leetcode-cn.com/problems/calculate-digit-sum-of-a-string/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 6070.py
@Time : 2022/04/17 22:27:48
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        l = len(s)
        while len(s) > k:
            tmp = ""
            num = 0
            l = len(s)
            for i in range(l):
                if i != 0 and i % k == 0:
                    tmp += str(num)
                    num = 0
                num += int(s[i])
            tmp += str(num)
            s = tmp
            print(s)
        return s