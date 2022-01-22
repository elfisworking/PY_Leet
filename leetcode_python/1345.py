# 1345. 跳跃游戏 IV
# https://leetcode-cn.com/problems/jump-game-iv/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1345.py
@Time : 2022/01/21 12:04:07
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Hard
'''
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        same_value_idx = defaultdict(list)
        for index, v in enumerate(arr):
            same_value_idx[v].append(index)
        d = deque()
        visited = set()
        d.append([0, 0])
        visited.add(0)
        while d:
            index, step = d.popleft()
            if index == len(arr) - 1:
                return step
            visited.add(index)
            for j in same_value_idx[arr[index]]:
                if j not in visited:
                    d.append([j, step + 1])
                    visited.add(j)
            del same_value_idx[arr[index]]
            if index + 1 not in visited:
                d.append([index + 1, step + 1])
                visited.add(index + 1)
            if 0 <= index - 1 and index - 1 not in visited:
                d.append([index -1, step + 1])
                visited.add(index - 1)
        return -1