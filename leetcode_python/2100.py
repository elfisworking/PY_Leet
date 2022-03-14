# 2100. 适合打劫银行的日子
# https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2100.py
@Time : 2022/03/06 20:14:53
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        l = len(security)
        if time == 0:
            return [i for i in range(l)]
        dp1 = [1] * l
        dp2 = [1] * l
        for i in range(1, l):
            if security[i] <= security[i - 1]:
                dp1[i] += dp1[i - 1]
        for i in range(l -2, -1, -1):
            if security[i] <= security[i + 1]:
                dp2[i] += dp2[i + 1]
        ans = []
        time += 1
        for i in range(1, l - 1):
            if dp1[i] >= time and dp2[i]  >= time:
                ans.append(i)
        return ans
