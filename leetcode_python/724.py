from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        currentSum = 0
        total = sum(nums)
        for i in range(len(nums)):
            val = 2*currentSum + nums[i]
            if ( val== total):
                return i
            currentSum += nums[i]
        return -1
s = Solution()
print(s.pivotIndex([-1,-1,-1,-1,-1,0]))