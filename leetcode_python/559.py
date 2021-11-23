
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/
# 559. N 叉树的最大深度
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 559.py
@Time : 2021/11/21 16:59:27
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0      
        ans = 0
        def dfs(node, i):
            if not node.children:
                nonlocal ans
                ans = max(ans, i)
                return
            for child in node.children:
                dfs(child, i + 1)
        dfs(root, 1)
        return ans