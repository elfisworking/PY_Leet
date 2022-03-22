# 657. 机器人能否返回原点
# https://leetcode-cn.com/problems/robot-return-to-origin/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 657.py
@Time : 2022/03/21 20:16:52
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = Counter(moves)
        if counter["U"] == counter["D"] and counter["L"] == counter["R"]:
            return True
        return False