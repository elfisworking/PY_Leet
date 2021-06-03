# 1707. 与数组中元素的最大异或值
# https://leetcode-cn.com/problems/maximum-xor-with-an-element-from-array/
# 可以将这条题目与421题合起来看 体会体会
from typing import List
class Trie:
    L  = 30
    def __init__(self):
        self.left = None
        self.right = None
    
    def insert(self,val:int):
        node = self
        for i in range(Trie.L,-1,-1):
            bit = (val >> i) & 1
            # 左边放0
            if bit == 0:
                if not node.left:
                    node.left = Trie()
                node = node.left
            else:
                if not node.right:
                    node.right = Trie()
                node = node.right
    def getMaxXor(self,val:int) -> int:
        ans , node = 0 ,self
        for i in range(Trie.L,-1,-1):
            bit = (val >> 1) & 1
            check = False
            if bit == 0:
                # 当为0时，优先取右边 相当于取反 要不然取取左边
                if node.right:
                    node = node.right
                    check = True
                else:
                    node = node.left
            else:
                if node.left:
                    node = node.left
                    check = True
                else:
                    node = node.right
            if check:
                ans |= 1 << i
        return ans

class Solution:
    # 超时 直接暴力进行求解的话
    # def maximizeXor_burst(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    #     ans = []
    #     nums.sort()
    #     for i in queries:
    #         if i[1]< nums[0] :
    #             ans.append(-1)
    #         else:
    #             tmp = -1
    #             for val in nums:
    #                 if val <= i[1]:
    #                     tmp = max(tmp,val^i[0]) 
    #                 else:
    #                     break
    #             ans.append(tmp)
    #     return ans
    
    # 想到了字典树的解法 但是不会写 以下为官方的解法
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n ,q = len(nums),len(queries)
        nums.sort()
        queries = sorted([(x,m,i) for i , (x,m) in enumerate(queries)],key=lambda k:k[1])
        ans = [0]*q
        t= Trie()
        idx = 0
        for x, m ,qid in queries:
            while idx < n and nums[idx] < m:
                t.insert(nums[idx])
                idx += 1
            if idx == 0:
                ans[qid] = -1
            else:
                ans[qid] = t.getMaxXor(x)
        return ans

