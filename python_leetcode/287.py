# 287. 寻找重复数
# https://leetcode-cn.com/problems/find-the-duplicate-number/
from typing import List
from collections import defaultdict
class Solution:
    # 使用散列表的方式进行计数
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
            if d[i] >= 2:
                return i
        return -1
