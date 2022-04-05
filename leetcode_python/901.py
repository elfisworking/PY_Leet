# 901. 股票价格跨度
# https://leetcode-cn.com/problems/online-stock-span/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 901.py
@Time : 2022/03/19 21:05:30
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        ans = self.day - self.stack[-1][1] if self.stack else self.day + 1
        self.stack.append((price, self.day))
        self.day += 1
        return ans  


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)