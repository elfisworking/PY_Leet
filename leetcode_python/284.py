# 284. 窥探迭代器
# https://leetcode-cn.com/problems/peeking-iterator/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 284.py
@Time : 2021/10/05 17:43:19
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : simulation, using one variable store peek element
'''
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = iterator.next()
        self._hasNext = iterator.hasNext()

    def peek(self):
        return self._next

    def next(self):
        ret = self._next
        self._hasNext = self.iterator.hasNext()
        self._next = self.iterator.next() if self._hasNext else 0
        return ret

    def hasNext(self):
        return self._hasNext
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].