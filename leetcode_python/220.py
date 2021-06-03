# 220. 存在重复元素 III
# https://leetcode-cn.com/problems/contains-duplicate-iii/
from sortedcontainers import SortedList
import bisect
from typing import List
class Solution:
    # 暴力方法超时
    # def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    #     l = len(nums)
    #     for a in range(l):
    #         for  b in range(a+1,l):
    #             n = abs(b-a)
    #             if n > k:
    #                 break
    #             else:
    #                 v = abs(nums[b]-nums[a])
    #                 if v <= t:
    #                     return True
    #     return False
    # 使用了TreeSet这个数据结构
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # O(N logk)
        window = SortedList()
        for i in range(len(nums)):
            # len(window) == k
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx] - window[idx-1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx+1] - window[idx]) <= t:
                return True
        return False
