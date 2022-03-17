# 2027. 转换字符串的最少操作次数
# https://leetcode-cn.com/problems/minimum-moves-to-convert-string/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2027.py
@Time : 2022/03/15 16:51:17
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def minimumMoves(self, s: str) -> int:
        right = 0
        l = len(s)
        ans = 0
        while right < l and s[right] == "O":
            right += 1
        left = right
        while right < l:
            while right < l and s[right] != "O":
                right += 1
            sub = right - left
            ans += sub // 3
            mod = sub % 3
            if mod == 2:
                ans += 1
            elif mod == 1:
                if right + 1 < l:
                    s[right + 1] == "X"
                    right = right + 2
                ans += 1
            while right < l and s[right] == "O":
                right = right + 1
            left = right
        
        return ans