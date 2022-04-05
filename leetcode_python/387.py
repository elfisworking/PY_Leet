# 387. 字符串中的第一个唯一字符
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 387.py
@Time : 2022/03/20 20:46:59
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def firstUniqChar(self, st: str) -> int:
        alphabet = defaultdict(int)
        s = dict()
        for index, val in enumerate(st):
            if val not in s:
                s[val] = index
            alphabet[val] += 1
        l = len(st)
        ans = l
        for key, val in alphabet.items():
            if val == 1:
                ans = min(ans, s[key])
        return ans if ans != l else -1