# 1743. 从相邻元素对还原数组
# https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 1743.py
@Time : 2021/07/25 13:21:13
@Author : YuMin Zhang
'''
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        h = defaultdict(list)
        for i in adjacentPairs:
            h[i[0]].append(i[1])
            h[i[1]].append(i[0])
        
        start_element = None
        pair_element = None
        for a ,b in h.items():
            if len(b) == 1:
                start_element = a
                pair_element = b[0]
                break
        print(h)
        print(start_element,pair_element)
        ans = [start_element,pair_element]

        while True:
            pair_elements =  h[pair_element]
            if len(pair_elements) == 1:
                break
 
            for i in pair_elements:
                if i != start_element:
                    ans.append(i)
                    start_element = pair_element
                    pair_element = i
                    break
        
        return ans
            
s = Solution()
print(s.restoreArray([[2,1],[3,4],[3,2]]))