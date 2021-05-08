# 1011. 在 D 天内送达包裹的能力
# https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left , right = max(weights),sum(weights)
        def check(limit):
            val = 0
            today = 1
            for i in weights:
                if val+i <= limit:
                    val += i
                else:
                    today += 1
                    val = i
            # 这里注意是要 小于等于D
            if today <= D and val <= limit:
                return True
            return False
            
        while left < right:
            mid = (left+right)//2
            print(left,right,mid)
            if  check(mid):
                right = mid
            else:
                left = mid + 1
        return left
s = Solution()
print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))