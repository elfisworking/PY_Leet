# 1576. 替换所有的问号
# https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1576.py
@Time : 2022/01/05 10:34:13
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy
'''
class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        if n == 1 and s == "?":
            return "a"
        res = list(s)
        for i in range(n):
            if res[i] == "?":
                for j in "abc":
                    if i == 0:
                        if res[i+1] != j:
                            res[i] = j
                            break
                    elif i == n - 1:
                        if res[i - 1] != j:
                            res[i] = j
                    else:
                        if res[i + 1] != j and j != res[i -1]:
                            res[i] = j
                            break
        return "".join(res)