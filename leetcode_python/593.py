# 593. 有效的正方形
# https://leetcode-cn.com/problems/valid-square/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 593.py
@Time : 2022/03/12 22:04:36
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        d = defaultdict(int)
        point = [p1, p2, p3, p4]
        for i in range(4):
            for j in range(i + 1, 4):
                distance = pow((point[i][0] - point[j][0]), 2) + pow((point[i][1] - point[j][1]), 2)
                d[distance] += 1
        dis = list(d.items())
        if len(dis) != 2:
            return False
        dis.sort()
        if dis[0][0] * 2 == dis[1][0] and dis[0][1] == 4 and dis[1][1] == 2:
            return True
        return False 