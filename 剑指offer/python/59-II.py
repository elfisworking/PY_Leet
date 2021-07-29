# 剑指 Offer 59 - II. 队列的最大值
# https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 59-II.py
@Time : 2021/07/28 11:25:34
@Author : YuMin Zhang
@State : Nonindepedent | Independent | Half-independent
@Thinking : 
'''
class MaxQueue:

    def __init__(self):
        self.queue = deque()
        self.heap = []

    def max_value(self) -> int:
        if not self.queue:
            return -1
        return self.heap[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        heapq.heappush(self.heap,-value)

    def pop_front(self) -> int:
        return self.queue.popleft()
        



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()