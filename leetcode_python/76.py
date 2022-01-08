# 76. 最小覆盖子串
# https://leetcode-cn.com/problems/minimum-window-substring/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
from collections import Counter
'''
@File : 76.py
@Time : 2022/01/08 18:13:26
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag :Hard
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        counter = Counter(t)
        def check():
            for i in counter.values():
                if i > 0:
                    return False
            return True 
        ans = len(s) + 1
        l, r = None, None
        while right < len(s):
            if s[right] in counter:
                counter[s[right]] -= 1
            if check():
                while True:
                    if s[left] in counter:
                        if counter[s[left]]  < 0:
                            counter[s[left]] += 1
                        else:
                            break
                    left += 1
                        
                if right - left + 1 < ans:
                    ans = right - left + 1
                    l = left
                    r = right
                if s[left] in counter:
                    counter[s[left]] += 1
                left += 1
            right += 1
        if l != None:
            return s[l: r + 1]

        return ""
s = Solution()
print(s.minWindow("a", "a"))