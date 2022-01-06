# 面试题 02.05. 链表求和
# https://leetcode-cn.com/problems/sum-lists-lcci/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 02.05.py
@Time : 2022/01/04 19:43:19
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        ans = ListNode(0)
        tmp_node = ans
        while l1 and l2:
            num = l2.val + l1.val + carry 
            carry = num // 10
            tmp = ListNode(num % 10)
            tmp_node.next = tmp
            tmp_node = tmp_node.next
            l1 = l1.next
            l2 = l2.next        
        if l1:
            while l1 and carry != 0:
                num = l1.val + carry
                carry = num // 10
                l1.val = num % 10
                tmp_node.next = l1
                tmp_node = tmp_node.next
                l1 = l1.next
            if l1:
                tmp_node.next = l1
        elif l2:
            while l2 and carry != 0:
                num = l2.val + carry
                carry = num // 10
                l2.val = num % 10
                tmp_node.next = l2
                tmp_node = tmp_node.next
                l2 = l2.next
            if l2:
                tmp_node.next = l2

        if carry != 0:
            tmp_node.next = ListNode(carry)
        return ans.next
