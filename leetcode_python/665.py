from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        l = len(nums)
        ans = 0
        for i in range(l-1):
            if nums[i] > nums[i+1]:
                if i+1>1:
                    if nums[i+1]<nums[i-1]:
                        nums[i+1]=nums[i]
                ans += 1
                if ans>=2:
                    return False
        return True 
            
s = Solution()
print(s.checkPossibility([3,4,2,3])) 