# 剑指 Offer 16. 数值的整数次方
# https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/
class Solution:
    # 一开始写的解法
    def myPow_myself(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        res = 0
        flag = False
        if n < 0:
            flag = True
        if abs(n)%2 == 0:
            y = self.myPow_myself(x,abs(n)//2)
            res = y*y
        else:
            y = self.myPow_myself(x,(abs(n)-1)//2)
            res = y*y*x
        if flag:
            return 1/res
        return res

        # 使用快速幂的解法
    def myPow(self,x:float,n:int)->float:
        if x == 0:
            return 0
        res = 1
        if n < 0: 
            x, n = 1/x,-n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res 