# 剑指 Offer 58 - I. 翻转单词顺序
# https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 58-1.py
@Time : 2021/07/26 15:11:59
@Author : YuMin Zhang
@State : Nonindepedent | Independent | Half-independent
@Thinking : 栈的思想
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        stack = []
        for ch in s:
            stack.append(ch)
        ans = []
        while stack:
            ch = stack.pop()
            ans.append(ch)
        
        return " ".join(ans)

s = Solution()
print(s.reverseWords("aa bb  ccc"))