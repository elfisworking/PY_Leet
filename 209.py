# 209. 长度最小的子数组
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/
from typing import List
import bisect
class Solution:
    # 滑动窗口的方法
    def minSubArrayLen_slide(self, target: int, nums: List[int]) -> int:
        vals = sum(nums)
        if vals < target:
            return 0
        left , right = 0 , 0
        val = 0
        res = l = len(nums)
        while right < l :
            val += nums[right]
            while val >= target:
                res = min(right - left +1,res)
                val -= nums[left]
                left += 1
                
            right += 1

        return res
    # 二分搜索 和 前缀和 结合使用
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])
        
        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))
        
        return 0 if ans == n + 1 else ans
    

