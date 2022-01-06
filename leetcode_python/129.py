# 129. 求根节点到叶节点数字之和
# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 129.py
@Time : 2022/01/04 21:04:13
@Author : YuMin Zhang
@State : Indepeedent
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
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        ans = 0
        def dfs(node, num):
            if node.left == None and node.right == None:
                nonlocal ans
                num = num * 10 + node.val
                ans += num
            num = num * 10 + node.val
            if node.left:
                dfs(node.left, num)
            if node.right:
                dfs(node.right, num)
        dfs(root, 0)
        return ans
