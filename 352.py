# 532. 数组中的 k-diff 数对
# https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/description/
from typing import List
class Solution:
    # 另外还可以使用hash的方法
    # 注意 a+b = k 可以转化为 b= k-a
    # 要牢记
    def findPairs(self, nums: List[int], k: int) -> int:
        l = len(nums)
        nums.sort()
        if l < 2 or (nums[-1]-nums[0])<k:
            return 0
        res = 0
        left = 0 
        right = left+1
        while right < l:
            if (nums[right]-nums[left]) == k:
                if (right - left) == 1:
                    res += 1
                else:
                    if right > 0 and nums[right-1] != nums[right]:
                        res += 1
                right += 1
            elif (nums[right]-nums[left]) <k :
                right += 1
            else:
                left += 1
            
            if left == right:
                right = left + 1
        return res