# 剑指 Offer 06. 从尾到头打印链表
# https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        tail = head
        ans  = []
        while tail != None:
            ans.append(tail.val)
            tail = tail.next
        return ans[::-1]
        