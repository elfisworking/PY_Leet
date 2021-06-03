# 783. 二叉搜索树节点最小距离
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ans = math.inf
        pre = -1
        def dfs(root:TreeNode,ans,pre) :
            if root is None:
                return 
            dfs(root.right,ans,pre)
            if pre == -1:
                pre = root.val
            else:
                ans = min(ans,root.val-pre)
                pre = root.val
            dfs(root.left,ans,pre)
        dfs(root,ans,pre)
        return ans




        