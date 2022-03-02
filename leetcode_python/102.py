# 102. 二叉树的层序遍历
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 102.py
@Time : 2022/02/20 22:14:20
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        d = deque()
        d.append(root)
        ans = []
        while d:
            tmp_d = deque()
            tmp_l = []
            while d:
                node = d.popleft()
                tmp_l.append(node.val)
                if node.left:
                    tmp_d.append(node.left)
                if node.right:
                    tmp_d.append(node.right)
            d= tmp_d
            ans.append(tmp_l)
        return ans