# 1716. 计算力扣银行的钱
# https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1716.py
@Time : 2022/01/15 19:33:27
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
'''
class Solution:
    def totalMoney(self, n: int) -> int:
        if n < 7:
            return int((1 + n) * n / 2)
        total = (1 + 7 ) * 7 / 2
        a = n // 7
        c = (total * a + a * (a - 1) * 7 / 2)
        b = n % 7
        d = (1 + a ) * b  + b * (b - 1) / 2
        ans = c + d
        return int(ans)
