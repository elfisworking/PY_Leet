# 1944. 队列中可以看到的人数
# https://leetcode-cn.com/problems/number-of-visible-people-in-a-queue/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1944.py
@Time : 2022/03/19 21:13:54
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        if not heights:
            return []
        l = len(heights)
        ans = [0] * l
        stack = []
        for i in range(l - 1, -1, -1):
            tmp = 0
            while stack and stack[-1][0] < heights[i]:
                stack.pop()
                tmp += 1
            ans[i] = tmp 
            ans[i] += 1 if stack else 0
            stack.append((heights[i], i))
        return ans 