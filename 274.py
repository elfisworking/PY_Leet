# 274. H 指数
# https://leetcode-cn.com/problems/h-index/
# 275 II
from typing import List
class Solution:
    def hIndex_myself(self, citations: List[int]) -> int:
        citations.sort()
        l = len(citations)
        def check(limit):
            if l-limit <= citations[limit]:
                return True
            return False 
        left , right = 0 , len(citations)
        while left< right:
            mid = (right-left)//2 + left
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return l - left
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        l = len(citations)
        def check(limit):
            val = 0
            for i in range(l-1,-1,-1):
                if citations[i] >= limit:
                    val += 1
                # 注意大于等于的符号
                if val >  limit and l - val <  limit:
                    return True
            return False 
        left , right = 0 , len(citations)
        while left < right:
            mid = (right-left)//2 + left
            if check(mid):
                left = mid + 1
            else:
                right = mid 
        return l-left
s = Solution()
print(s.hIndex_myself([1,2,3,4,5]))