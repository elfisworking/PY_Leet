# 1996. 游戏中弱角色的数量
# https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1996.py
@Time : 2022/01/28 23:16:02
@Author : YuMin Zhang
@State : Half-Depedent
@Thinking :
@Tag : Medium
'''
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x : (-x[0], x[1]))
        maxDef = properties[0][1]
        ans = 0
        for i in properties:
            if i[1] < maxDef:
                ans += 1
            else:
                maxDef = i[1]
        return ans


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        stack = []
        properties.sort(key = lambda x:(x[0], -x[1]))
        ans = 0
        stack.append(properties[0][1])
        for i in range(1, len(properties)):
            while stack and stack[-1] < properties[i][1]:
                stack.pop()
                ans += 1
            stack.append(properties[i][1])
        return ans