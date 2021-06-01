# 231. 2 的幂
# https://leetcode-cn.com/problems/power-of-two/
class Solution:
    # 使用了循环来解决这道题目
    def isPowerOfTwo_loop(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n%2 == 1:
                return False
            n = n/2
        return True
    
    def isPowerOfTwo_bit_operation(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0