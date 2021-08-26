# 881. 救生艇
# https://leetcode-cn.com/problems/boats-to-save-people/
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left , right = 0 , len(people) -1
        res = 0 
        while left < right:
            if people[right] + people[left] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1
            res += 1
        if left == right:
            
            res += 1
        return res


s = Solution()
print(s.numRescueBoats([3,5,3,4],5))
