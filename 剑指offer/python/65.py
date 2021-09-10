# 剑指 Offer 65. 不用加减乘除做加法
# https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/
class Solution:
    def add(self,a:int,b:int) -> int:
        x = 0xffffffff
        a, b = a & x ,b & x
        while b != 0:
            a , b = (a ^ b) , (a & b) << 1 & x
        return a if  a <= 0x7fffffff else ~(a ^ x)