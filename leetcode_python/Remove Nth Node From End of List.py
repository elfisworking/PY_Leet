class Solution:
    # 使用递归的方式 十分的巧妙
    # def removeNthFromEnd_1(self, head, n):
    #     global i 
    #     if head is None:
    #         i=0
    #         return None
    #     head.next = self.removeNthFromEnd(head.next,n)
    #     i+=1
    #     return head.next if i==n else head
    # 第二种方法 使用快慢指针
    def removeNthFromEnd(self,head,n):
        newHead = ListNode(0,head)
        fastPointer = head
        for i in range(n):
            fastPointer = fastPointer.next
        slowPointer = newHead
        while fastPointer!=None:
            fastPointer=fastPointer.next
            slowPointer=slowPointer.next
        slowPointer.next = slowPointer.next.next
        return head
    #第三种方法就是 两边循环 一次获得链表的长度 一次删去节点