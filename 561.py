from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        ans = 0
        for i in range(0,l,2):
            ans += nums[i]
        return ans
s = Solution()
print(s.arrayPairSum([1,4,3,2]))