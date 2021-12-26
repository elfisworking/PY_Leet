# 1078. Bigram 分词
# https://leetcode-cn.com/problems/occurrences-after-bigram/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1078.py
@Time : 2021/12/26 12:23:36
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
'''
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        ans = []
        if len(text) < 3:
            return []
        ans = []
        for i in range(2, len(text)):
            if text[i - 2] == first and text[i - 1] == second:
                ans.append(text[i])
        return ans