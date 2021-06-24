# 剑指 Offer 03. 数组中重复的数字
# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
from typing import List
class Solution:
    # 使用思想：hash表
    def findRepeatNumber(self, nums: List[int]) -> int:
        my_dict ={}
        for num in nums:
            if num in my_dict:
                return num
            else:
                my_dict[num]=1
