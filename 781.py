from typing import List
from collections import defaultdict
import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = defaultdict(int)
        for i in answers:
            i = i+1
            d[i] = d[i] + 1
        num = 0
        for k, v in d.items():
            if k >= v:
                num +=k
            else:
                a = math.ceil(v/k)
                num += a*k
        return num
s = Solution()
print(s.numRabbits([1,1,1,0,4]))