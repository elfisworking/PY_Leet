# [342] 4的幂
# https://leetcode-cn.com/problems/power-of-four/
class Solution:
    def isPowerOfFour_loop(self, n: int) -> bool:
        if n < 1:
            return False
        while n != 1:
            if n % 4 != 0:
                return False
            n /= 4
        return True 
    
    # 先判断是否是2的幂，然后4^x = (3+1)^x 
    # (3+1)^x mod 3 = 1 mod 3    
    def isPowerOfFour_mod(self, n: int) -> bool:
        return n > 0 and n&(n-1) == 0 and n%3 == 1