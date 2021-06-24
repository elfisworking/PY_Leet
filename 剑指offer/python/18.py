# 剑指 Offer 18. 删除链表的节点
# https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            head = head.next
            return head
        tmp , b = head.next, head
        while tmp:
            if tmp.val == val:
                break
            b = tmp 
            tmp = tmp.next
        b.next = tmp.next
        return head
        