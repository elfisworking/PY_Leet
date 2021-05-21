# 剑指 Offer 14- I. 剪绳子
# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/
# 切分规则：
# 最优： 3 。把绳子尽可能切为多个长度为3 的片段，留下的最后一段绳子的长度可能为 0,1,2 三种情况。
# 次优： 2 。若最后一段绳子长度为 2 ；则保留，不再拆为 1+1 。
# 最差： 1 。若最后一段绳子长度为 1 ；则应把一份 3 + 1替换为 2 + 2，因为 2 * 2 > 3 * 1。
import math
class Solution:
    def cuttingRope(self, n: int) -> int:
        # 可以使用递归的方法
        # 但是是否还有其它方法??
        # 数学方法
        # 推论一： 将绳子 以相等的长度等分为多段 ，得到的乘积最大。
        # 推论二： 尽可能将绳子以长度 33 等分为多段时，乘积最大
        # 
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)