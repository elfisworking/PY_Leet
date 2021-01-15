from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        if l<=3:
            return []
        res = []
        for i in range(l-3):
            if i >0 and nums[i]==nums[i-1]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target:
                break
            if nums[i]+nums[l-1]+nums[l-2]+nums[l-3] < target:
                continue
            t = target-nums[i]
            for x  in range(i+1,l-2):
                if x>i+1 and nums[x]==nums[x-1]:
                    continue
                if nums[i] + nums[x] + nums[x + 1] + nums[x + 2] > target:
                    break
                if nums[i] + nums[x] + nums[l - 2] + nums[l - 1] < target:
                    continue
                left = x + 1
                right = l-1
                while left < right:
                    value = nums[x]+nums[left]+nums[right]
                    if value == t:
                        res.append([nums[i],nums[x],nums[left],nums[right]])
                        while left<right and nums[right-1]==nums[right]:
                            right -= 1
                        while left<right and nums[left+1]==nums[left]:
                            left +=1
                        right -= 1
                        left += 1
                    elif value > t:
                        right -= 1
                    else:
                        left += 1
        return res
s = Solution()
print(s.fourSum([-2,-1,-1,1,1,2,2],0))