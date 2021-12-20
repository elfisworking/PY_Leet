# 475. 供暖器
# https://leetcode-cn.com/problems/heaters/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 475.py
@Time : 2021/12/20 13:40:39
@Author : YuMin Zhang
@State : Indepeedent
@Thinking : binary search
@Tag : Medium
'''
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        right = int(1e9)
        left = 0
        l = len(houses)
        def check(radius, l):
            j = 0
            for i in heaters:
                while j < l and i - radius <= houses[j] <= i + radius:
                    j += 1
                if j == l:
                    return True
            return False
        while left < right:
            mid = left + (right - left) // 2
            if check(mid, l):
                right = mid
            else:
                left = mid + 1
        return right

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            j = bisect_right(heaters, house)
            i = j - 1
            rightDistance = heaters[j] - house if j < len(heaters) else float('inf')
            leftDistance = house - heaters[i] if i >= 0 else float('inf')
            curDistance = min(leftDistance, rightDistance)
            ans = max(ans, curDistance)
        return ans

# sort & double pointer
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        houses.sort()
        heaters.sort()
        j = 0
        for i, house in enumerate(houses):
            curDistance = abs(house - heaters[j])
            while j + 1 < len(heaters) and abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1]):
                j += 1
                curDistance = min(curDistance, abs(houses[i] - heaters[j]))
            ans = max(ans, curDistance)
        return ans
