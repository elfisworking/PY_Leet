# 606. 根据二叉树创建字符串
# https://leetcode-cn.com/problems/construct-string-from-binary-tree/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 606.py
@Time : 2022/03/19 20:32:56
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        ans = []
        def dfs(node):
            if not node:
                return 
            ans.append(str(node.val))
            if node.right or node.left:
                ans.append("(")
                dfs(node.left)
                ans.append(")")
                if node.right:
                    ans.append("(")
                    dfs(node.right)
                    ans.append(")")
        dfs(root)
        return "".join(ans)