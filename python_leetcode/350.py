# 350. 两个数组的交集 II
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/
from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return re

s = Solution()
print(s.intersect([1,2,2,1],[2,2]))