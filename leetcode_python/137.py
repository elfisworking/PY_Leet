from collections import defaultdict
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h =  defaultdict(int)
        for n in nums:
           h[n] += 1
        print(h)
        for k,v in h.items():
            if v == 1:
                return k
    def singleNumber_1(self,nums:List[int]):
        counts = [0]*32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res , m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31-i] %3
        return res
s = Solution()
print(s.singleNumber_1([2,2,3,2]))