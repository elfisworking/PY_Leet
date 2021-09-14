# https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
# 剑指 Offer 61. 扑克牌中的顺子
from typing import List
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        counter = 0
        new_nums = []
        for i in nums:
            if i == 0:
                counter += 1
            else:
                new_nums.append(i)
        new_nums.sort()
        for i in range(len(new_nums)-1):
            if new_nums[i] +  1 != new_nums[i+1]:
                sub = new_nums[i+1] - new_nums[i] - 1
                if sub > 0 and counter >= sub:
                    counter -= sub
                else:
                    return False
        return True