# 1518. 换酒问题
# https://leetcode-cn.com/problems/water-bottles/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1518.py
@Time : 2021/12/17 13:50:48
@Author : YuMin Zhang
@State : Indepeedent 
@Thinking :
@Tag : Easy
'''
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            a = numBottles // numExchange
            numBottles = numBottles % numExchange + a
            ans += a
        return ans
