# 477. 汉明距离总和
# https://leetcode-cn.com/problems/total-hamming-distance/
from typing import List 
class Solution:
    # 这个方法以空间换了时间
    # 比较直接
    # 与官方解题思路大体一致 
    def totalHammingDistance_first_solution(self, nums: List[int]) -> int:
        res = 0
        for _ in range(30):
            one = 0
            zero = 0
            for i  in range(len(nums)) :
                val = nums[i] & 1
                nums[i] = (nums[i]>>1)
                if val == 1:
                    one += 1
                else:
                    zero += 1
            res += one * zero
        return res