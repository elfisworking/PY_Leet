# 剑指 Offer 07. 重建二叉树
# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        l = len(preorder)
        def myBuildTree(pre_left,pre_right,in_left,in_right):
            # 递归终止条件
            if pre_left > pre_right:
                return None
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            in_root = index[root_val]
            size_left_subtree = in_root-in_left
            root.left = myBuildTree(pre_left+1,pre_left+size_left_subtree,in_left,in_root-1)
            root.right = myBuildTree(pre_left+size_left_subtree+1,pre_right,in_root+1,in_right)
            return root

        index = {element:i for i,element in enumerate(inorder)}
        return myBuildTree(0,l-1,0,l-1)

            