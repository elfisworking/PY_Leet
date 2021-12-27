# 825. 适龄的朋友
# https://leetcode-cn.com/problems/friends-of-appropriate-ages/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
from collections import Counter
'''
@File : 825.py
@Time : 2021/12/27 20:18:24
@Author : YuMin Zhang
@State : Half-Depedent
@Thinking :
@Tag : Medium
'''
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if len(ages) == 0: return 0
        ans = 0
        ages.sort()
        left = 0
        for i in range(1, len(ages)):
            a = 0.5 * ages[i] + 7
            while ages[left] <= a and left < i:
                left += 1
            ans += i - left 
            print(ans, left)
        counter = Counter(ages)
        for value , i in counter.items():
            if value >= 15 and i > 1:
                ans += i * ( i - 1) // 2
        return ans

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        n = len(ages)
        ages.sort()
        left = right = ans = 0
        for age in ages:
            if age < 15:
                continue
            while ages[left] <= 0.5 * age + 7:
                left += 1
            while right + 1 < n and ages[right + 1] <= age:
                right += 1
            ans += right - left
        return ans


s = Solution()
print(s.numFriendRequests([73,106,39,6, 26,15,30,100,71,35,46,112,6,60,110]))