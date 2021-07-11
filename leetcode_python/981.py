# 981. 基于时间的键值存储
# https://leetcode-cn.com/problems/time-based-key-value-store/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 981.py
@Time : 2021/07/10 22:00:48
@Author : YuMin Zhang
'''
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.d[key]
        if not values:
            return ""
        left , right  = 0 , len(values)-1
        while left < right:
            mid = left + (right-left + 1)//2
            if values[mid][1] <= timestamp:
                left = mid 
            else:
                right = mid-1
                
        return values[left][0] if values[left][1] <= timestamp else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)