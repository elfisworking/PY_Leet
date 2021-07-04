# 645. 错误的集合
# https://leetcode-cn.com/problems/set-mismatch/
from typing import List
class Solution:
    # 使用哈希的思想解决
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        s = {i for i in range(1,l+1)}
        ans = []
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                ans.append(i)
        s = list(s)
        ans.append(s[0])
        return ans
    
    # 使用数学的方法解决
    def findErrorNums_math(self, nums: List[int]) -> List[int]:
        ln, total = len(nums), sum(set(nums))
        return [sum(nums) - total, (1 + ln) * ln // 2 - total]