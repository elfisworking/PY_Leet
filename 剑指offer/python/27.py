# 剑指 Offer 27. 二叉树的镜像
# https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        d = deque()
        d.append(root)

        while d:
            node = d.popleft()
            node.right , node.left = node.left,node.right
            if node.right:
                node.append(node.right)
            if node.left:
                node.append(node.left)
        
        return  root