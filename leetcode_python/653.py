# 653. 两数之和 IV - 输入 BST
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
from collections import Counter
'''
@File : 653.py
@Time : 2022/03/21 20:13:01
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        vals = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)
        dfs(root)
        left = 0
        right = len(vals) - 1
        while left < right:
            val = vals[left] + vals[right]
            if val == k:
                return True
            elif val > k:
                right -= 1
            else:
                left += 1
        return False