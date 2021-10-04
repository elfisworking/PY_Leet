# 1436. 旅行终点站
# https://leetcode-cn.com/problems/destination-city/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 1436.py
@Time : 2021/10/04 14:17:16
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city = {}
        for i in paths:
            if i[0] not in city:
                city[i[0]] = 0
            if i[1] not in city:
                city[i[1]] = 0
            
            city[i[0]] += 1
        
        for k ,v in city.items():
            if v == 0:
                return k