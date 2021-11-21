# 563. 二叉树的坡度
# https://leetcode-cn.com/problems/binary-tree-tilt/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 563.py
@Time : 2021/11/18 22:28:28
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node):
            if not node:
                return 0
            right = dfs(node.right)
            left = dfs(node.left)
            nonlocal ans
            ans += abs(right - left)
            return left + right + node.val
        dfs(root)
        return ans 