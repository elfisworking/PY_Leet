# 86. 分隔链表
# https://leetcode-cn.com/problems/partition-list/
from curses.ascii import SO
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 86.py
@Time : 2022/01/25 22:08:04
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        dummy_less = ListNode(0)
        dummy_greater = ListNode(0)
        tmp_less = dummy_less
        tmp_greater = dummy_greater
        while head:
            if head.val < x:
                tmp_less.next = head
                tmp_less = tmp_less.next
            else:
                tmp_greater.next = head
                tmp_greater = tmp_greater.next
            print(head.val)
            head = head.next
        print(tmp_greater.val)
        tmp_greater.next = None
        tmp_less.next = dummy_greater.next
        return dummy_less.next 
x = ListNode(2)
y = ListNode(1)
x.next = y
s = Solution()
print(s.partition(x, 2))