# https://leetcode-cn.com/problems/w3tCBm/
# 剑指 Offer II 003. 前 n 个数字二进制中 1 的个数
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(1,n+1):
            if i % 2 == 0:
                res[i] = res[i//2]
            else:
                res[i] = res[i-1] + 1
        return res



        