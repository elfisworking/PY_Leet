# 剑指 Offer 17. 打印从1到最大的n位数
# https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
from typing import List
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        maxVlaue = 10**n
        res = []
        for i in range(1,maxVlaue):
            res.append(i)
        return res