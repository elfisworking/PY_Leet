# 671. 二叉树中第二小的节点
# https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 671.py
@Time : 2021/07/27 16:01:07
@Author : YuMin Zhang
@State : Half-independent
@Thinking : search way,
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # error
    # def findSecondMinimumValue(self, root: TreeNode) -> int:
    #     if (root.left == None and root.right == None) or (root.left.val == root.right.val):
    #         rteurn -1
    #     return root.left.val if root.val > root.left.val else root.right.val
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        s = set()
        def dfs(root):
            s.add(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        s = list(s)
        if len(s) <= 1:
            return -1
        heapq.heapify(s)
        heapq.heappop(s)
        return s[0]