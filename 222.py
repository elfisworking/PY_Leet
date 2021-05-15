# 222. 完全二叉树的节点个数
# https://leetcode-cn.com/problems/count-complete-tree-nodes/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 递归搜索 O(n)
    def countNodes_recursive(self, root: TreeNode) -> int:
        if not root:
            return 0

        def count(node):
            
            if node.left == None and node.right == None:
                return 1
            res = 1
            if node.left != None:
                res += count(node.left)
            if node.right != None:
                res += count(node.right)
            return res

        return count(root)
    # binary_search && bit compution
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 0
        node = root
        while node.left != None:
            level += 1
            node =node.left
        def check(mid):
            bits = 1<<(level-1)
            node = root
            while node != None and bits> 0:
                if bits & mid == 0:
                    node = node.left
                else:
                    node = node.right
                bits >>= 1
            return node != None
        left , right = 1 << level, 1<<(level+1)-1
        while left < right:
            mid = (right-left)//2+left
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left