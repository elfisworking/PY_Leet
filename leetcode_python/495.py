# 495. 提莫攻击
# https://leetcode-cn.com/problems/teemo-attacking/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 495.py
@Time : 2021/11/10 22:47:10
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        experied = 0
        for i in timeSeries:
            if i >= experied:
                ans += duration
            else:
                ans += i + duration - experied
            experied = i + duration 
        return ans
            