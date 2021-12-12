# 911. 在线选举
# https://leetcode-cn.com/problems/online-election/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 911.py
@Time : 2021/12/12 20:04:35
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        tops = []
        voteCounts = defaultdict(int)
        voteCounts[-1] = -1
        top = -1
        for p in persons:
            voteCounts[p] += 1
            if voteCounts[p] >= voteCounts[top]:
                top = p
            tops.append(top)
        self.tops = tops
        self.times = times


    def q(self, t: int) -> int:
        left, right = 0, len(self.times)
        while left < right:
            mid = left + (right - left) // 2 # 这是一个取上界
            if self.times[mid] > t:
                right = mid
            else:
                left = mid + 1
        return self.tops[left - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)