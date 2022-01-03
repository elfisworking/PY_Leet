# 390. 消除游戏
# https://leetcode-cn.com/problems/elimination-game/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 390.py
@Time : 2022/01/02 13:46:13
@Author : YuMin Zhang
@State : Depedent 
@Thinking :
@Tag : Medium
'''
class Solution:
    def lastRemaining(self, n: int) -> int:
        a1 = 1
        k, cnt, step = 0, n, 1
        while cnt > 1:
            if k % 2 == 0:  # 正向
                a1 += step
            else:  # 反向
                if cnt % 2:
                    a1 += step
            k += 1
            cnt >>= 1
            step <<= 1
        return a1