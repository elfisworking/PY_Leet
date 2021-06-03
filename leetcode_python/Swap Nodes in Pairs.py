# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        zeroP = dummy
        oneP = head
        secondP = head.next
        while True:
            oneP.next = secondP.next
            zeroP.next = secondP
            secondP.next= oneP
            temp = oneP
            oneP = secondP
            secondP = temp
            if not secondP.next or not secondP.next.next:
                break
            secondP = secondP.next.next
            oneP = oneP.next.next
            zeroP = zeroP.next.next
        return dummy.next
    def swapPairs_1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = head.next
        head.next = self.swapPairs(newhead.next)
        newhead.next = head
        return newhead
s = Solution()
li = ListNode(3,ListNode(4,None))
li = ListNode(2,li)
li = ListNode(1,li)
print(s.swapPairs(li))
