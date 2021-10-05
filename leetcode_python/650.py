# 650. 只有两个键的键盘
# https://leetcode-cn.com/problems/2-keys-keyboard/
# 不会做
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        i = 2
        while i * i <= n:
            while n % i == 0:
                ans += i
                n = n//i
            i += 1
        if n != 1:
            ans += n
        return ans