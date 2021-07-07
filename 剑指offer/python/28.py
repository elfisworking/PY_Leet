# 剑指 Offer 28. 对称的二叉树
# https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def recursive(l,r):
            if not l and not r:
                return True

            if not l and r:
                return False
            if not r and l:
                return False
            if l.val != r.val:
                return False
                
            return recursive(l.left,r.right) and recursive(l.right,r.left)
        return recursive(root.left,root.right)

        