def find_mid_point(node):
    if not node:
        return None
    slow = node
    fast = node
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow