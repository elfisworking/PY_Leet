# 剑指 Offer 30. 包含min函数的栈
# https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
'''
@File : 30.py
@Time : 2021/07/07 11:33:30
@Author : YuMin Zhang
'''
# 使用了一个辅助栈进行存储的最小值
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]