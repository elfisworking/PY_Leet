# https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
# 剑指 Offer 66. 构建乘积数组
from typing import List
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        l = len(a)
        b = [1]* l
        tmp = 1
        for i in range(1,l):
            b[i] = b[i-1] * a[i-1]
        for i in range(l-2,-1,-1):
            tmp *= a[i+1]
            b[i] *= tmp
        return b

