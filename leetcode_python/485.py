from typing import List
class Solution:
    # 采用了双指针的做法
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = len(nums)
        left,right = 0,0
        ans =  0
        while right<l:
            if nums[right] == 1:
                right += 1
            else:
                ans = max(ans,right-left)
                right +=1
                left = right
        ans = max(ans,right-left)
        return ans
    # 直接暴力的解法
    def findMaxConsecutiveOnes_1(self, nums: List[int]) -> int:
        nums.append(0)
        cur = 0
        res = 0
        for num in nums:
            if num:
                cur += 1
            else:
                res = max(res, cur)
                cur = 0
        return res
s = Solution()
print(s.findMaxConsecutiveOnes([]))