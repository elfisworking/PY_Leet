# 725. 分隔链表
# https://leetcode-cn.com/problems/split-linked-list-in-parts/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        l = 0
        tmp = head
        while tmp:
            l += 1
            tmp = tmp.next
        a , b = l // k , l % k
        res = []
        if a == 0:
            while head:
                next = head.next
                head.next = None
                res.append(head)
                head = next
            for _ in range(b,k):
                res.append(None)
        else:
            for i in range(k):
                res.append(head)
                part_size = a + (1 if i < b else 0)
                for j in range(1,part_size):
                    head = head.next
                next = head.next
                head.next = None
                head = next
        return res
