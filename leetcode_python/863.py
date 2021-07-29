# 863. 二叉树中所有距离为 K 的结点
# https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 863.py
@Time : 2021/07/28 09:43:21
@Author : YuMin Zhang
@State : Nonindepedent
@Thinking : 
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        d = dict()
        
        def dfs(node:TreeNode):
            if node.left:
                d[node.left.val] = node
                dfs(node.left)
            if node.right:
                d[node.right.val] = node
                dfs(node.right)
            
        def findAns(node:TreeNode,parent:TreeNode,depth:int):
            if not node:
                return 
            if depth == k:
                ans.append(node.val)
                return 
            if node.left != parent:
                findAns(node.left,node,depth+1)
            if node.right != parent:
                findAns(node.right,node,depth+1)
            if node.val in d and d[node.val] != parent:
                findAns(d[node.val],node,depth+1)
        
        dfs(root)
        findAns(target,None,0)  
        
        return ans
            


