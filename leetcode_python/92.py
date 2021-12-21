# 92. 反转链表 II
# https://leetcode-cn.com/problems/reverse-linked-list-ii/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 92.py
@Time : 2021/12/21 20:44:32
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
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right: return head
        pre = None
        lnode = head
        rnode = head
        for i in range(1, right):
            if i < left:
                pre = lnode
                lnode = lnode.next
            rnode = rnode.next
        lpre = rnode.next
        end = rnode.next
        while lnode != end:
            tmp = lnode.next
            lnode.next = lpre
            lpre = lnode
            lnode = tmp
        if pre:
            pre.next = rnode
        return head if left != 1 else rnode
