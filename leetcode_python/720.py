# 720. 词典中最长的单词
# https://leetcode-cn.com/problems/longest-word-in-dictionary/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 720.py
@Time : 2022/03/17 10:11:31
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
# Error
# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         if not words:
#             return ""
#         words.sort()
#         l = len(words)
#         i = 0
#         flag = False
#         length = 0
#         ans = ""
#         while i < l:
#             if flag:
#                 if i > 0 and  words[i - 1] + words[i][-1]  == words[i]:
#                     if len(words[i]) > length:
#                         length = len(words[i])
#                         ans = words[i]
#                 else:
#                     flag = False      
#             if len(words[i]) == 1:
#                 if length == 0:
#                     length = 1
#                 if not ans:
#                     ans = words[i]
#                 flag = True
#             i += 1
#         return ans        
class Tire:
    def __init__(self, depth, is_end):
        self.is_end = is_end
        self.d = defaultdict(Tire)
        self.depth = depth
        self.length = 0
        self.ans = ""
    
    def insert(self, word):
        cur = self
        flag = True
        for ch in word:
            if ch not in cur.d:
                cur.d[ch] = Tire(cur.depth + 1, False)
            if not cur.is_end:
                flag = False
            cur = cur.d[ch]
        if flag:
            if cur.depth > self.length:
                self.length = cur.depth
                self.ans = word
        cur.is_end = True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        root = Tire(0, True)
        for word in words:
            root.insert(word)
        return root.ans
s = Solution()
print(s.longestWord(["w","wo","wor","worl", "world"]))