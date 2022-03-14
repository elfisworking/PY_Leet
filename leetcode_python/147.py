# 147. 对链表进行插入排序
# https://leetcode-cn.com/problems/insertion-sort-list/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 147.py
@Time : 2022/03/10 15:26:46
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummyNode = ListNode(-5001)
        tmp = head
        dummyNode.next = tmp
        tmp = tmp.next
        dummyNode.next.next = None
        while tmp:
            point = dummyNode.next
            prev = dummyNode
            while point and point.val < tmp.val:
                prev = point
                point = point.next
            prev.next = tmp
            tmp = tmp.next
            prev.next.next = point
        return dummyNode.next