from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        sum = 99999
        res = 0
        for i in range(l-1):
            right = l-1
            left = i + 1 
            while left < right:
                value = nums[i]+nums[right]+nums[left]
                sub = 0
                if value>target:
                    right -= 1
                    sub= value - target
                elif value< target:
                    left += 1
                    sub  = target - value
                else:
                    return target
                if sum > sub :
                    sum = sub
                    res = value    
        return res
s = Solution()
print(s.threeSumClosest([-1,2,1,-4],2))
