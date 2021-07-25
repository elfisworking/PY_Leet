# 面试题 10.02. 变位词组
# https://leetcode-cn.com/problems/group-anagrams-lcci/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 10.01.py
@Time : 2021/07/25 21:18:22
@Author : YuMin Zhang
@Thinking : 字符串哈希
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for i in strs:
            tmp = list(i)
            tmp.sort()
            tmp = "".join(tmp)
            h[tmp].append(i)
        
        ans = []
        for i in h.values():
            ans.append(i)
        
        return ans
