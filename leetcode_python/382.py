# 382. 链表随机节点
# https://leetcode-cn.com/problems/linked-list-random-node/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 382.py
@Time : 2022/01/16 10:25:24
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.d = dict()
        self.size = self.setDict(head)

    def getRandom(self) -> int:
        idx = random.randint(0, self.size - 1)
        return self.d[idx].val

    def setDict(self, head):
        count = 0
        while head:
            self.d[count] = head
            count += 1
            head = head.next
        return count
        



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()