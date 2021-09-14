# 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p , q = q, p 
        res = None
        def dfs(node):
            nonlocal res
            if not node or res:
                return 
            if p.val <= node.val <= q.val:
                res = node
                return 
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res