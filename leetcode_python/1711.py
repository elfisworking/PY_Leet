# 1711. 大餐计数
# https://leetcode-cn.com/problems/count-good-meals/
from typing import List
from collections import defaultdict
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        mod = 1000000007
        maxVal = max(deliciousness) * 2
        d = defaultdict(int)

        for val in deliciousness:
            s = 1 
            while s <= maxVal:
                count = d[s-val]
                ans = (count + ans)%mod
                s = s << 1
            d[val] += 1


        return ans
