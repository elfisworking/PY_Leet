# 138. 复制带随机指针的链表
# https://leetcode-cn.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # 自己完成的 通过两个映射表 来完成random关系的映射
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        copy_head = new_head = Node(head.val)
        link_hash = {}
        copy_hash = {}
        copy_hash[head] = copy_head
        if head.random:
            link_hash[copy_head] = head.random
        head = head.next
        while head:
            copy_next = Node(head.val)
            copy_hash[head] = copy_next
            if head.random:
                link_hash[copy_next] = head.random
            copy_head.next = copy_next
            copy_head = copy_next
            head = head.next

        for n , ran in link_hash.items():
            if ran in copy_hash:
                n.random = copy_hash[ran]
        return new_head

    # 官方的一种方法 不需要使用map表，十分的巧妙 
    def copyRandomList_offical(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old


