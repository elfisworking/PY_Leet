# 剑指 Offer II 077. 链表排序
# https://leetcode-cn.com/problems/7WHec2/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : offerII077.py
@Time : 2022/04/19 22:00:00
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
    def sortList(self, head: ListNode) -> ListNode:
        def merge_sort(head):
            if not head.next:
                return head
            prev = None
            slow = head
            fast = head
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            prev.next = None
            l1 = merge_sort(head)
            l2 = merge_sort(slow)
            dummy_Node = ListNode()
            ans = dummy_Node
            while l1 and l2:
                if l1.val < l2.val:
                    dummy_Node.next = l1
                    l1 = l1.next
                    dummy_Node.next.next = None
                else:
                    dummy_Node.next = l2
                    l2 = l2.next
                    dummy_Node.next.next = None
                dummy_Node = dummy_Node.next
            while l1:
                dummy_Node.next = l1
                l1 = l1.next
                dummy_Node.next.next = None
                dummy_Node = dummy_Node.next
            while l2:
                dummy_Node.next = l2
                l2 = l2.next
                dummy_Node.next.next = None
                dummy_Node = dummy_Node.next
            return ans.next
        if not head:
            return None
        return merge_sort(head)
