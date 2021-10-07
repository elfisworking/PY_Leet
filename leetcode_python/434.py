# 434. 字符串中的单词数
# https://leetcode-cn.com/problems/number-of-segments-in-a-string/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 434.py
@Time : 2021/10/07 12:56:01
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : brute algorithm
'''
class Solution:
    # brute algorithm
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        s = s.split()
        return len(s)
