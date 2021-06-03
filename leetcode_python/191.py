# 191. 位1的个数
# https://leetcode-cn.com/problems/number-of-1-bits/
# 考察 二进制操作 与 或 异或
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += n & 1
            n  = n >> 1
        return res