# 1609. 奇偶树
# https://leetcode-cn.com/problems/even-odd-tree/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1609.py
@Time : 2021/12/25 18:08:31
@Author : YuMin Zhang
@State : Indepeedent
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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        d = deque()
        d.append(root)
        length = 1
        flag = True
        while d:
            tmp = None
            l = length
            length = 0
            for i in range(l):
                if i == 0:
                    node = d.popleft()
                    tmp = node.val
                    if flag and tmp % 2 == 0:
                        return False
                    if not flag and tmp % 2 == 1:
                        return False
                    if node.left:
                        length += 1
                        d.append(node.left)
                    if node.right:
                        length += 1
                        d.append(node.right)
                else:
                    node = d.popleft()
                    if flag:
                        if tmp < node.val and  node.val % 2 == 1:
                            tmp = node.val
                        else:
                            return False
                    else:
                        if tmp > node.val and node.val % 2 == 0:
                            tmp = node.val
                        else:
                            return False
                    if node.left:
                        length += 1
                        d.append(node.left)
                    if node.right:
                        length += 1
                        d.append(node.right)
                if i == l - 1:
                    flag = not flag
        return True
                        
