# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        q = deque()
        res = []
        if not root:
            return res
        res.append(root.val)
        q.append(root)
        while q:
            node = q.popleft()
            if node.left:
                res.append(node.left.val)
                q.append(node.left)
            if node.right:
                res.append(node.right.val)
                q.append(node.right)
            
        return res