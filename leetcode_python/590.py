# 590. N 叉树的后序遍历
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 590.py
@Time : 2022/03/12 21:35:36
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
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return root
        ans = []
        def dfs(node):
            for i in node.children:
                dfs(i)
            ans.append(node.val)
            
        dfs(root)    
        return ans

