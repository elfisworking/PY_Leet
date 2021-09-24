# 430. 扁平化多级双向链表
# https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        tmp_head = head
        def dfs(pre,head):
            while head:
                if head.child:
                    head.child.prev = head
                    node = dfs(None,head.child)
                    pre = node
                    pre.next = head.next
                    if head.next:
                        head.next.prev = pre 
                    head.next = head.child
                    head.child = None
                    head = pre.next
                else:
                    pre = head
                    head = head.next
            return pre
        dfs(None,tmp_head)
        return head