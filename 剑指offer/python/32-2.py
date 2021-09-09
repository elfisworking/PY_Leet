# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = deque()
        res = []
        if not root:
            return res
        q.append(root)
        q.append(1)
        while q:
            tmp = []
            while True:
                node = q.popleft()
                if node == 1:
                    if q:
                        q.append(1)
                    break
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if tmp:
                res.append(tmp)
        return res