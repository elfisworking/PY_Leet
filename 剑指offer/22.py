# 剑指 Offer 22. 链表中倒数第k个节点
# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 也是双指针的问题，但是这次是快慢指针
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 快慢指针
        if not head:
            return head
        slow = head
        fast = head
        for _ in range(k-1):
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        return slow