# 735. 行星碰撞
# https://leetcode-cn.com/problems/asteroid-collision/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 735.py
@Time : 2022/03/08 14:51:31
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if not stack:
                stack.append(i)
                continue
            if stack[-1] < 0 and i < 0:
                stack.append(i)
            elif i > 0:
                stack.append(i)
            else:
                while stack:
                    if stack[-1] + i == 0:
                        stack.pop()
                        break
                    elif stack[-1] + i > 0:
                        break
                    else:
                        stack.pop()
                        if not stack or stack[-1] < 0:
                            stack.append(i)
                            break

        return stack