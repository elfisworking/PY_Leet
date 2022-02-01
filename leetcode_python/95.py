# 95. 不同的二叉搜索树 II
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 95.py
@Time : 2022/01/25 21:51:42
@Author : YuMin Zhang
@State : Depedent 
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(left, right):
            if left > right:
                return [None]
            all_trees = []
            for i in range(left, right + 1):
                left_trees = dfs(left, i - 1)
                right_trees = dfs(i + 1, right)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
            return all_trees
        return dfs(1, n) if n > 0 else []