# 875. 爱吃香蕉的珂珂
# https://leetcode-cn.com/problems/koko-eating-bananas/
from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = sum(piles)//h, max(piles)
        if left == 0:
            left = 1
        def check(limit):
            time = 0
            for i in piles:
                time += ceil(i/limit)
            if time <= h:
                return True
            return False
        while left < right:
            mid  = (left+right)//2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
