# 142. 环形链表 II
# https://leetcode-cn.com/problems/linked-list-cycle-ii/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 使用Set的方法 但是这个方法使用了O(n)的空间
    def detectCycle_set(self, head: ListNode) -> ListNode:
        ptr = head
        s = set()
        while ptr != None:
            if ptr in s:
                return ptr
            else:
                s.add(ptr)
            ptr = ptr.next
        return None
    # 另外 还可以使用 快慢指针的方式来确认位置
    # 对于 slow fast 这两个指针
    # 有着如下的的说明推理：
    # 当 slow到达环的入口时，即为在位置0处，此时fast指针在换的位置b处，两者相距b步的距离
    # 设环的总长度为c
    # 那么当两个指针相遇时，满足此式 b+2t-t=c 其中t为slow指针所走的步数
    # 那么 t=c-b，从而我们可以得知 快慢指针必在slow还没走完一圈时相遇
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow  = fast = head
        while fast != None:
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:# 这里还是挺重要的 要不然会有测试样例过不去
                return None
            if fast == slow:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None

        
