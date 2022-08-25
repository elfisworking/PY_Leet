# 6062. 设计一个 ATM 机器
# https://leetcode-cn.com/problems/design-an-atm-machine/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 6062.py
@Time : 2022/04/17 23:11:40
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class ATM:

    def __init__(self):
        self.nums = [0] * 5
        self.d = {0 : 20, 1 : 50, 2 : 100, 3: 200, 4:500}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.nums[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        tmp  = self.nums[:]
        for i in range(4, -1, -1):
            if tmp[i] == 0:
                continue
            m = self.d[i]
            a = amount // m
            b = amount % m
            if a > tmp[i]:
                amount = (a -tmp[i]) * m + b
                ans[i] = tmp[i]
                tmp[i] = 0
            else:
                tmp[i] -= a
                amount = b
                ans[i] = a
            if amount == 0:
                self.nums = tmp
                return ans
        return [-1]



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)