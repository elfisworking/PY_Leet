# 859. 亲密字符串
# https://leetcode-cn.com/problems/buddy-strings/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 859.py
@Time : 2021/11/23 22:20:15
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        l1 = len(s)
        l2 = len(goal)
        if l1 < 1 or l2 < 1:
            return False
        if l1 != l2:
            return False
        left, right = 0, l1 - 1
        while left < l1:
            if s[left] != goal[left]:
                break
            left += 1
        if left == l1:
            counter = Counter(goal)
            for i in counter.items():
                if i[1] > 1:
                    return True
            return False
        while left < right:
            if s[right] != goal[right]:
                break
            right -= 1
        if s[left] == goal[right] and s[right] == goal[left]:
            left += 1
            while left < right:
                if s[left] != goal[left]:
                    return False
                left += 1
            return True
        return False
    
        def buddyStrings_others(self, s: str, goal: str) -> bool:
        l1 = len(s)
        l2 = len(goal)
        if l1 != l2:
            return False
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        sum = 0
        for i in range(l1):
            d1[s[i]] += 1
            d2[goal[i]] += 1
            if s[i] != goal[i]:
                sum +=1 

        flag = False
        for key, value in d1.items():
            if d2[key] != value:
                return False
            if value > 1:
                flag = True
        
        return sum == 2 or (sum == 0 and flag)
        
