# 633. 平方数之和
# https://leetcode-cn.com/problems/sum-of-square-numbers/
from math import floor
from math import ceil
class Solution:
    # 第一种方法 暴力 不过容易超时  
    def judgeSquareSum_brust(self, c: int) -> bool:
        s = floor(pow(c,0.5)+1)
        # print(s)
        for a in range(s):
            b = pow(c-a**2,0.5)
            if b == int(b):
                return True
        return False 
    # 傻逼没有想到双指针的解法 抽象一下明显就是双指针的题型
    def judgeSquareSum(self, c: int) -> bool:
        right  = pow(c,0.5)
        left = 0
        while left<=right:
            number = left**2 + right**2
            if number == c:
                return True
            elif number>c:
                right -= 1
            else:
                left += 1
        return False
        