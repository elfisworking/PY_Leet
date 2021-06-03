# 461 汉明距离
# https://leetcode-cn.com/problems/hamming-distance/solution/yi-ming-ju-chi-by-leetcode-solution-u1w7/
class Solution:
    # 暴力 直接进行比较
    def hammingDistance_first_solution(self, x: int, y: int) -> int:
        res = 0
        for i in range(31):
            x_bit = x & (1<<i)
            y_bit = y & (1<<i)
            if x_bit != y_bit :
                res += 1
        return res
    
    # 先将x和y异或，比较异或结果二进制中有几个1。因为出现1的话，说明
    # x和y在此位置符号不相等
    def hammingDistance_second_solution(self, x: int, y: int) -> int:
        xor = x ^ y
        res = 0
        while xor != 0:
            val = xor & 1
            if val == 1:
                res += 1
            xor = xor >> 1
        return res
    
    # 本方法是对第二个方法的优化，使用了Brian Kernighan 算法
    # 其结论如下：
    #结论：记 f(x) 表示 x 和 x-1 进行与运算所得的结果(即 f(x)=x & (x-1) )，那么 f(x) 恰为 x 删去其二进制表示中最右侧的 1的结果。

    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        res = 0
        while xor != 0:
            xor &= xor - 1
            res += 1
        return res 