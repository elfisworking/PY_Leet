# 124. 二叉树中的最大路径和
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 124.py
@Time : 2021/12/29 23:05:38
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Hard
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def divide(node):
            nonlocal ans
            if not node:
                return 0
            lval = divide(node.left)
            rval = divide(node.right)
            tmp = max(node.val, lval + node.val)
            tmp =  max(tmp, rval + node.val)
            ans = max(ans, tmp)
            ans = max(ans, rval + lval + node.val)
            return tmp
        divide(root)
        return ans