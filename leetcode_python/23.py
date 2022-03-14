# 23. 合并K个升序链表
# https://leetcode-cn.com/problems/merge-k-sorted-lists/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 23.py
@Time : 2022/03/14 16:55:12
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy_node = ListNode()
        tmp = dummy_node
        while True:
            min_value = float("inf")
            min_node = None
            for index, node in enumerate(lists):
                if node and node.val < min_value:
                    min_value = node.val
                    min_node = index
            # print(min_node)
            # print(lists)
            if min_node != None:
                tmp.next = lists[min_node]
                lists[min_node] = lists[min_node].next
                tmp.next.next = None
                tmp = tmp.next
            else:
                break
        return dummy_node.next
                