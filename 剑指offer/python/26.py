# 剑指 Offer 26. 树的子结构
# https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/
# Definition for a binary tree node.
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return False
        d = deque()
        d.append(A)
        
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        while d:
            node = d.popleft()
            if node.val == B.val:
                if recur(node,B):
                    return True
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)
        
        return False