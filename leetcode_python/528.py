# https://leetcode-cn.com/problems/random-pick-with-weight/
# 528. 按权重随机选择
from typing import List
import random
from itertools import accumulate
from bisect import bisect_left
class Solution:
    # 超时
    # def __init__(self, w: List[int]):
    #     self.s = sum(w)-1
    #     self.l = []
    #     for index , value in enumerate(w):
    #         for _ in range(value):
    #             self.l.append(index)


    # def pickIndex(self) -> int:
    #     x = random.randint(0,self.s)
    #     return self.l[x]

    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        self.total = sum(w)

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return bisect_left(self.pre, x)