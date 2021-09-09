# 剑指 Offer 55 - II. 平衡二叉树
# https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isBalanced(self,root:TreeNode) -> bool:
        def height(root:TreeNode):
            if not root:
                return 0
            return max(height(root.left),height(root.right)) + 1
        
        if not root:
            return True
        return abs(height(root.left)-height(root.right)) and self.isBalanced(root.left) and self.isBalanced(root.right)
