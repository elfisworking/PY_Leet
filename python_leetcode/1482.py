# 1482. 制作 m 束花所需的最少天数
# https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets/
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = len(bloomDay)
        if l < m*k:
            return -1
        day = set(bloomDay)
        l = len(day)
        day = list(day)
        day.sort()
        def check(limit):
            total_count = 0
            count = 0
            for i in bloomDay:
                if i <= limit:
                    count += 1
                    if count == k:
                        count = 0
                        total_count += 1
                        if total_count == m:
                            return True
                            break
                else:
                    count = 0

            if total_count == m:
                return False
            return False
        print(day)
        left ,right = 0, l
        while  left < right:
            mid = (left+right)//2
            if check(day[mid]):
                right = mid
            else:
                left = mid + 1
        return day[left]


