# 61. 旋转链表
# https://leetcode-cn.com/problems/rotate-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 思路：闭合为链 寻找切割点
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if k == 0:
            return head
        tail = head
        length = 1
        while tail.next != None:
            length += 1
            tail = tail.next
        # 将首位相连
        tail.next = head
        index  = length-(k%length)
        split_point = head

        for _ in range(index-1):
            split_point = split_point.next
        new_head = split_point.next
        split_point.next = None
        return new_head
