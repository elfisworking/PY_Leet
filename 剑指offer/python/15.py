# 剑指 Offer 15. 二进制中1的个数
# https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/
# 考察 二进制操作 与 或 异或
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += n & 1
            n  = n >> 1
        return res