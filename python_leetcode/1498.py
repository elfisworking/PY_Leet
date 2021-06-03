# 1498. 满足条件的子序列数目
# https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
# 输入：nums = [3,5,6,7], target = 9
# 输出：4
# 解释：有 4 个子序列满足该条件。
# [3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0] * 2 > target:
            return 0
        left , right = 0 , len(nums)-1
        res = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += 2**(right-left)
                left += 1
            else:
                right -= 1
        return res%(10**9 + 7)
        

s = Solution()
print(s.numSubseq([1,5,6,2],6))

