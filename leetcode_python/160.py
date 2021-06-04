# 160. 相交链表
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 暴力方法 两边循环 O(n)
    def getIntersectionNode_brute_way(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        if not headA or not headB:
            return None
        h1 = headA
        h2 = headB
        while h1:
            s.add(h1)
            h1 = h1.next
        while h2:
            if h2 in s:
                return h2
            h2 = h2.next
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        ptr1 = headA
        ptr2 = headB
        while ptr1 != ptr2:
            ptr1 = ptr1.next if ptr1 else headB
            ptr2 = ptr2.next if ptr2 else headA
        return ptr1
