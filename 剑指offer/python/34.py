from typing import List
# Definition for a binary tree node.
# 剑指 Offer 34. 二叉树中和为某一值的路径
# https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(node,tar):
            if not node:
                return 
            path.append(node.val)
            tar += node.val
            # 不能这样 因为会有负数target的情况
            # if tar > target:
            #     path.pop()
            #     return 
            if tar == target and  node.left == None and node.right == None:
                res.append(path[:])

            dfs(node.left,tar)
            dfs(node.right,tar)
            path.pop()
        dfs(root,0)
        return res
