# 剑指 Offer 44. 数字序列中某一位的数字
# https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
class Solution:
    # def findNthDigit(self, n: int) -> int:
    #     # 使用模拟的方法进行结果
    #     # 但是超时
    #     i = -1
    #     num = 0
    #     while True:
    #         s = str(num)
    #         i += len(s)
    #         if i >= n:
    #             return int(s[n-i-1])
    #         num += 1
    def findNthDigit(self, n: int) -> int:
        digit , start , count = 1, 1, 9
        while n  > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n-1) // digit
        return int(str(num)[(n-1) % digit])