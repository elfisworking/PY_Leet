# 141. 环形链表
# https://leetcode-cn.com/problems/linked-list-cycle/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 注意这里面的判断的
        if not head or not head.next:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            # 注意这里面的结束条件
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True