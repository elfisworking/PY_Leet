# 剑指 Offer II 004. 只出现一次的数字 
# https://leetcode-cn.com/problems/WGki4K/
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0]*32
        for i in nums:
            for a in range(32):
                bits[a] +=  i & 1
                i >>= 1

        res = 0
        for i in range(32):
    
            res <<= 1
            res |= bits[31-i]%3

        return res if bits[31]%3 == 0 else ~(res ^ 0xffffffff)
s = Solution()
print(s.singleNumber([1,1,1,3]))
            