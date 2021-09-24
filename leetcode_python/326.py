# 326. 3的幂
# https://leetcode-cn.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        while n and n%3 == 0:
            n = n//3
            if n == 1:
                return True
        return False
