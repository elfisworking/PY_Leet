# 2034. 股票价格波动
# https://leetcode-cn.com/problems/stock-price-fluctuation/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2034.py
@Time : 2022/01/23 13:56:02
@Author : YuMin Zhang
@State : Half-Depedent
@Thinking :
@Tag : Medium
'''
class StockPrice:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.d = defaultdict(int)
        self.curr_val = 0
        self.curr_time = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp >= self.curr_time:
            self.curr_time = timestamp
            self.curr_val = price
        self.d[timestamp] = price
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.curr_val

    def maximum(self) -> int:
        while self.max_heap:
            price, time = self.max_heap[0]
            if -price == self.d[time]:
                return -price
            heappop(self.max_heap)
        return 0

    def minimum(self) -> int:
        while self.min_heap:
            price, time = self.min_heap[0]
            if price == self.d[time]:
                return price
            heappop(self.min_heap)
        return 0

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


# Your StockPrice object will be instantiated and called as such:
obj = StockPrice()
obj.update(4,2)
param_2 = obj.current()
param_3 = obj.maximum()
param_4 = obj.minimum()