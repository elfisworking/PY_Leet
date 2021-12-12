# 709. 转换成小写字母
# https://leetcode-cn.com/problems/to-lower-case/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 709.py
@Time : 2021/12/12 20:05:15
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for ch in s:
            if ord("A") <= ord(ch) <= ord("Z"):
                ans += chr(ord(ch) + 32)
            else:
                ans += ch
        return ans