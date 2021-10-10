#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 352.py
@Time : 2021/10/10 18:32:33
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : 维护了一个有序的数组
'''
class SummaryRanges:

    def __init__(self):
        self.l = []

    def addNum(self, val: int) -> None:
        if val not in self.l:
            bisect.insort_left(self.l, val)

    def getIntervals(self) -> List[List[int]]:
        inter = []
        tmp = [self.l[0]]
        for i in range(1, len(self.l)):
            if self.l[i] - 1 != self.l[i-1]:
                tmp.append(self.l[i-1])
                inter.append(tmp)
                tmp = [self.l[i]]
        tmp.append(self.l[-1])
        inter.append(tmp)
        return inter

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()