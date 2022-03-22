# 234. 回文链表
# https://leetcode-cn.com/problems/palindrome-linked-list/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 234.py
@Time : 2022/03/18 20:08:43
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
# O(n)
# O(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        left, right = 0 , len(val_list) - 1
        while left < right:
            if val_list[left] == val_list[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
# 找到终点
# 反转后面部分
# 进行比对
# O(n), O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast =  head, head
        prev = None
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        middle_right = slow.next
        while middle_right:
            tmp = middle_right.next
            middle_right.next = prev
            prev = middle_right
            middle_right =tmp
        while prev and head:
            if prev.val == head.val:
                prev = prev.next
                head = head.next
            else:
                return False
        return True