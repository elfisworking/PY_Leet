# 682. 棒球比赛
# https://leetcode-cn.com/problems/baseball-game/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 682.py
@Time : 2022/03/18 20:39:18
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in range(len(ops)):
            if ops[i] == "+":
                stack.append(stack[-1] + stack[-2])
            elif ops[i] == "D":
                stack.append(stack[-1] * 2)
            elif ops[i] == "C":
                stack.pop()
            else:
                stack.append(int(ops[i]))
        return sum(stack)
