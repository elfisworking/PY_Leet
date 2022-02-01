# 1342. 将数字变成 0 的操作次数
# https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1342.py
@Time : 2022/01/31 21:35:00
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num > 0:
            if num % 2 == 1:
                ans += 1
                num -= 1
            if num == 0:
                break
            num = num // 2
            ans += 1
        return ans
        