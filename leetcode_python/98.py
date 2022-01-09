# 98. 验证二叉搜索树
# https://leetcode-cn.com/problems/validate-binary-search-tree/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 98.py
@Time : 2022/01/09 21:52:19
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Medium
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        order = []
        def mid(root):
            if not root:
                return 
            mid(root.left)
            order.append(root.val)
            mid(root.right)
        mid(root)
        for i in range(1, len(order)):
            if order[i] <= order[i -1]:
                return False
        return True