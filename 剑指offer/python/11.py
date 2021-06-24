# 剑指 Offer 11. 旋转数组的最小数字
# https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l = len(numbers)
        if l == 1:
            return numbers[0]
        for i in range(1,l):
            if numbers[i-1]>numbers[i]:
                return numbers[i]
        return numbers[0]
        