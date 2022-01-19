# 236. 二叉树的最近公共祖先
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 236.py
@Time : 2022/01/16 12:15:59
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursion(node):
            if not node:
                return False
            l = recursion(node.left)
            r = recursion(node.right)
            if (l and r) or ((node.val == p.val or node.val == q.val) and (l or r)):
                self.ans = node
                
            return node.val == p.val or node.val == q.val or l or r
        recursion(root)
        return self.ans 