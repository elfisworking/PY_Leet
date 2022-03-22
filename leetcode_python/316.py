# 316. 去除重复字母
# https://leetcode-cn.com/problems/remove-duplicate-letters/
from typing import List
from collections import defaultdict
from collections import Counter
from math import inf
import bisect
import heapq
'''
@File : 316.py
@Time : 2022/03/21 20:34:14
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        visited  = set()
        for ch in s:
            if ch in visited:
                counter[ch] -= 1
                continue
            while stack and stack[-1] >= ch and counter[stack[-1]] > 0:
                pop_value = stack.pop()
                visited.remove(pop_value)
                
            stack.append(ch)
            visited.add(ch)
            counter[ch] -= 1
        return "".join(stack)
                    
s = Solution()
print(s.removeDuplicateLetters("cbacdcbc"))