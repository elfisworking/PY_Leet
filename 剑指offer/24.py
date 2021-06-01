# 剑指 Offer 24. 反转链表
# https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList_violent_way(self, head: ListNode) -> ListNode:
        if not head:
            return head
        l = []
        while head:
            l.append(head)
            head = head.next
        length = len(l)
        reverse_head = tmp = l[-1]
        for i in range(length-1,-1,-1):
            tmp.next = l[i]
            tmp = l[i]
        tmp.next = None
        return reverse_head 
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev