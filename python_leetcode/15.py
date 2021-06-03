# 三数之和
# https://leetcode-cn.com/problems/3sum/
# 重复次数 1
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l <= 2:
            return []
        nums.sort()
        res = []
        for i in range(l):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i]==nums[i-1]:
                continue
            L = i+1
            R= l -1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i]+nums[L]+nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L = L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R = R-1
                    L = L + 1
                    R = R -1
                elif nums[i]+nums[L]+nums[R]>0:
                    R = R -1
                else:
                    L = L + 1
        return res

    def threeSum_r1(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l<=2:
            return []
        nums.sort()
        res = []
        for i in range(l):
            if nums[i]>0:
                break
            if i >0 and nums[i-1] == nums[i]:
                continue
            left , right = i+1,l-1
            while left < right:
                if nums[left] > 0:
                    break
                val = nums[i]+nums[left]+nums[right]
                if val == 0:
                    res.append([nums[i],nums[left],nums[nums[right]]])
                    while left<right and nums[left]==nums[left+1]:
                        left = left + 1
                    while left<right and  nums[right-1]==nums[right]:
                        right = right -1
                    left = left + 1
                    right = right - 1
                elif val > 0:
                    right = right -1
                else:
                    left = left + 1
        return res

s = Solution()
print(s.threeSum_r1([0,0,0,0,1,-1]))
