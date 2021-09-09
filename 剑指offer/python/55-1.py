# Definition for a binary tree node.
#
# 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        if not root:
            return max_depth
        def dfs(node,curr_height):
            if not node:
                nonlocal max_depth
                max_depth = max(max_depth,curr_height)
                return 
            dfs(node.left , curr_height + 1)
            dfs(node.right, curr_height + 1)
        dfs(root,0)
        return max_depth