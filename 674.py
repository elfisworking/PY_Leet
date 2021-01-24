from typing import List
class Solution:
    # burst method
    def findLengthOfLCIS_1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp = 1
        ans = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                temp += 1
            else:
               ans = max(temp,temp)
               temp = 1
        ans = max(ans,temp)
        return ans
    # use dp
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        dp = [1] * l
        for i in range(1,l):
            if nums[i-1] < nums[i]:
                dp[i] = dp[i-1]  + 1
        ans = max(dp)
        return ans
s = Solution()
print(s.findLengthOfLCIS([2,2,2]))
