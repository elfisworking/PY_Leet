# 剑指 Offer 36. 二叉搜索树与双向链表
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 36.py
@Time : 2021/07/09 13:30:22
@Author : YuMin Zhang
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 中序遍历
        def mid(root):
            if root == None:
                return 
            mid(root.left)
            if self.pre:
                self.pre.right , root.left = root, self.pre
            else:
                self.head = root
            self.pre = root
            mid(root.right)
        if not root: return
        self.pre = None
        mid(root)
        self.head.left , self.pre.right = self.pre, self.head
        return self.head
