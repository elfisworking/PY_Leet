# 589. N 叉树的前序遍历
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 589.py
@Time : 2022/03/10 15:14:14
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        def dfs(node):
            ans.append(node.val)
            if node.children == None:
                return 
            for i in node.children:
                dfs(i)
        dfs(root)
        return ans