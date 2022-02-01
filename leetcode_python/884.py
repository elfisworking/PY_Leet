# 884. 两句话中的不常见单词
# https://leetcode-cn.com/problems/uncommon-words-from-two-sentences/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 884.py
@Time : 2022/01/30 21:09:36
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
'''
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        count_1 = Counter(s1)
        count_2 = Counter(s2)
        ans = []
        for i in s1:
            if count_1[i] == 1 and i not in count_2:
                ans.append(i)

        for i in s2:
            if count_2[i] == 1 and i not in count_1:
                ans.append(i)
        return ans 

