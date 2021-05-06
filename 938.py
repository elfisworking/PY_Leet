# 938. 二叉搜索树的范围和
# https://leetcode-cn.com/problems/range-sum-of-bst/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 二叉搜索树 中序遍历 范围
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        path = []
        def searchTree(root):
            if root.left != None:
                searchTree(root.left)
            if low<= root.val <= high:
                path.append(root.val)
            if root.right != None:
                searchTree(root.right)
        searchTree(root)
        return sum(path)
