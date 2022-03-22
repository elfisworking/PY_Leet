# 404. 左叶子之和
# https://leetcode-cn.com/problems/sum-of-left-leaves/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 404.py
@Time : 2022/03/16 22:10:19
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        def dfs(root, isleft):
            if root.left == None and root.right == None:
                if isleft:
                    nonlocal ans
                    ans += root.val
                return 
            if root:
                if root.left:
                    dfs(root.left, True)
                if root.right:
                    dfs(root.right, False)
        dfs(root, False)    
        return ans