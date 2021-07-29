#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 58-II.py
@Time : 2021/07/28 11:12:54
@Author : YuMin Zhang
@State : Nonindepedent | Independent | Half-independent
@Thinking : 
'''
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]