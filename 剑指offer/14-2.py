# 剑指 Offer 14- II. 剪绳子 II
# https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/
# python 无需考虑越界的问题
# 这一题比14-1这一题需要考虑int值越界问题
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, p = n // 3, n % 3, 1000000007
        if b == 0: return 3 ** a % p
        if b == 1: return 3 ** (a - 1) * 4 % p
        return 3 ** a * 2 % p