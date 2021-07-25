# https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
# 剑指 Offer 52. 两个链表的第一个公共节点
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 52.py
@Time : 2021/07/25 14:39:02
@Author : YuMin Zhang
@Thinking: 哈希表说一种思路，另外一种思路将其中一个连接成环,然后使用快慢指针
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     # 第一种思路,这种思路有一个问题，虽然时间复杂度为O(n),但是空间复杂度为O(n)
    #     tmp_headA = headA
    #     s = set()
        
    #     while tmp_headA:
    #         s.add(tmp_headA)
    #         tmp_headA = tmp_headA.next
        
    #     tmp_headB = headB
    #     while tmp_headB:
    #         if tmp_headB in s:
    #             return tmp_headB
    #         else:
    #             tmp_headB = tmp_headB.next
        
    #     return None
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        node1 = headA
        node2 = headB
        while node1!=node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1