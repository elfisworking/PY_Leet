# 剑指 Offer 33. 二叉搜索树的后序遍历序列
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
from typing import List
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i,j):
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j] : p += 1
            return p == j and recur(i,m-1) and recur(m,j-1)
        return recur(0,len(postorder)-1)
