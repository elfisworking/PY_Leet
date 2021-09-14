# 剑指 Offer 68 - II. 二叉树的最近公共祖先
# https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path1 = []
        path2 = []
        tmp = []
        def dfs(node,target,path):
            if not node or path:
                return node
            tmp.append(node)
            if node.val == target.val:
                path.extend(tmp[:])
                return            
            dfs(node.left,target,path)
            dfs(node.right,target,path)
            tmp.pop()
        dfs(root,p,path1)
        dfs(root,q,path2)
        l = min(len(path1),len(path2))
        for i in range(l-1,-1,-1):
            if path1[i] in path2:
                return path1[i]
        return None