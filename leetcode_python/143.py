#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 143.py
@Time : 2022/03/07 23:23:53
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dq = deque()
        dummyNode = ListNode()
        curr = dummyNode
        while head:
            dq.append(head)
            head = head.next
        while dq:
            node1 = dq.popleft()
            curr.next = node1
            node1.next = None
            curr = curr.next
            if dq:
                node2 = dq.pop()
                curr.next = node2
                node2.next = None
                curr = curr.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 空间复杂度O(1)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return 
        mid = self.getMiddle(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        dummyNode = ListNode()
        while l1 and l2:
            dummyNode.next = l1
            dummyNode = dummyNode.next
            l1 = l1.next
            dummyNode.next = l2
            l2 = l2.next
            dummyNode = dummyNode.next
        if l1:
            dummyNode.next = l1
        if l2:
            dummyNode.next = l2
        


    def reverseList(self, head:ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def getMiddle(self, head: ListNode)->ListNode:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

a = ListNode()
s = Solution()
print(s.reorderList(a))