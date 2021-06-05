# 203. 移除链表元素
# https://leetcode-cn.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        new_head = head
        prev = None
        while new_head:
            if new_head.val == val:
                prev.next = new_head.next
            else:
                prev = new_head    
            new_head = new_head.next 
        return head