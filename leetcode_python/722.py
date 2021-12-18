# 722. 删除注释
# https://leetcode-cn.com/problems/remove-comments/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 722.py
@Time : 2021/12/18 15:35:32
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        stage = 0
        pre = None
        for i in source:
            if stage != 2:
                s = ""
            for index, char in enumerate(i):
                if stage == 0 and char != "/":
                    s += char
                elif stage ==0  and char == "/":
                    pre = char
                    stage = 1
                elif stage == 1 and char == "/":
                    stage = 0
                    break
                elif stage == 1 and char == "*":
                    stage = 2
                elif stage == 1:
                    s += pre + char
                    stage = 0
                elif stage == 2 and char == "/" and pre == "*":
                    stage = 0
                elif stage == 2:
                    pre = char
            if s and stage != 2:
                if stage == 1 and pre:
                    s += pre
                    stage = 0
                ans.append(s)
        return ans
