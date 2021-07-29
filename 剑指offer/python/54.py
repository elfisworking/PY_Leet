#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 54.py
@Time : 2021/07/28 11:06:42
@Author : YuMin Zhang
@State : Nonindepedent | Independent | Half-independent
@Thinking : 
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        lt = list()
        def dfs(node:TreeNode):
            if not node:
                return 
            lt.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        lt.sort()
        return lt[-k]