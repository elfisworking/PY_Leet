# 二叉搜索树中第K小的元素
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     # 暴力求解  深度搜索 
#     # 二叉搜索树 中序遍历 无需排序
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         nodes = []
#         def dfs(node):
#             if node == None:
#                 return 
            
#             dfs(node.left)
#             nodes.append(node.val)
#             dfs(node.right)
        
#         dfs(root)
#         # nodes.sort()
#         return nodes[k-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 中序遍历
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 0
        result = None

        def inorder(node):
            nonlocal index, result

            if not node:
                return
            
            inorder(node.left)
            index += 1
            if index == k:
                result = node.val
                return
            inorder(node.right)

        inorder(root)
        return result
        