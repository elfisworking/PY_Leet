# 2038. 如果相邻两个颜色均相同则删除当前颜色
# https://leetcode-cn.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2038.py
@Time : 2022/03/22 10:09:07
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A_count = 0
        B_count = 0
        curr_ch = colors[0]
        left = 0
        right = 0
        while right < len(colors):
            if colors[right] == curr_ch:
                right +=1 
            else:
                if curr_ch == "A":
                    A_count += right - left - 2 if right - left - 2 > 0 else 0
                else:
                    B_count += right - left - 2 if right - left - 2 > 0 else 0                
                curr_ch = colors[right]
                left = right
        if curr_ch == "A":
            A_count += right - left - 2 if right - left - 2 > 0 else 0
        else:
            B_count += right - left - 2 if right - left - 2 > 0 else 0
        # print(A_count, B_count)
        if A_count > B_count:
            return True
        else:
            return False