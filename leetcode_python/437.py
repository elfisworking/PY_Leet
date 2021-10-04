# https://leetcode-cn.com/problems/path-sum-iii/
# 437. 路径总和 III
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 437.py
@Time : 2021/10/04 14:07:33
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : prefix and dfs
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = [0]
        res = 0
        def dfs(node):
            if not node:
                return
            nonlocal res 
            prefix.append(prefix[-1]+node.val)
            for i in range(len(prefix)-1):
                value = prefix[-1] - prefix[i]
                if value == targetSum:
                    res += 1    
            dfs(node.left)
            dfs(node.right)
            prefix.pop()

        dfs(root)
        return res  
