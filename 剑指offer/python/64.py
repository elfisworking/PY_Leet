# 剑指 Offer 64. 求1+2+…+n
# https://leetcode-cn.com/problems/qiu-12n-lcof/
class Solution:
    def sumNums(self, n: int) -> int:

        return n and (n + self.sumNums(n-1))