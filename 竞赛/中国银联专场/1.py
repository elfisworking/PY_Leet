# 银联-01. 回文链表
# https://leetcode-cn.com/contest/cnunionpay-2022spring/problems/D7rekZ/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 回文链表.py
@Time : 2022/03/17 22:17:24
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x = []
        tmp = head
        while tmp:
            x.append(tmp.val)
            tmp = tmp.next
        left, right = 0, len(x) - 1
        flag = 0
        while left < right:
            if x[left] == x[right]:
                left += 1
                right -= 1
            else:
                if left + 1 < right and x[left + 1] == x[right]:
                    flag += 1
                    if flag > 1:
                        return False
                    left += 2
                elif left < right - 1 and x[left] == x[right - 1]:
                    flag += 1
                    if flag > 1:
                        return False
                    right -= 2
                elif left == right - 1:
                    return True
                else:
                    return False
        return True
            