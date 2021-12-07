# 1816. 截断句子
# https://leetcode-cn.com/problems/truncate-sentence/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1816.py
@Time : 2021/12/07 09:33:29
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        s = s[:k]
        return " ".join(s)