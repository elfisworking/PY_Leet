# 525. 连续数组
# https://leetcode-cn.com/problems/contiguous-array/
from typing import List
class Solution:
    # 一开始想的是double pointer 
    # 但是感觉是前缀和 + 哈希
    # 可是没有想到如何在哈希表中寻找，
    # 看官方题解知道了如何在哈希表中寻找
    # 
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        prev = 0
        d = {0:-1}
        for index , v  in enumerate(nums):
            prev += 1 if v== 1 else -1
            if prev in d:
                ans = max(ans,index-d[prev])
            else:
                d[prev] = index
        return ans 