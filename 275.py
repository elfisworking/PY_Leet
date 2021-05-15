# 275. H 指数 II
# https://leetcode-cn.com/problems/h-index-ii/
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        left ,right = 0 ,l
        def check(mid):
            if l-mid <= citations[mid]:
                return True
            return False
        while left < right:
            mid = (right-left)//2 + left
            if check(mid):
                right = mid
            else:
                left = mid +1
        return l -left
s = Solution()
print(s.hIndex([1,2,100]))