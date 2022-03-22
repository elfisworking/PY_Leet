# 30. 串联所有单词的子串
# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 30.py
@Time : 2022/03/17 13:58:40
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        l = len(words)
        if len(s) < word_len * l:
            return []
        counter = Counter(words)
        total_len = word_len * l
        ans = []
        for i in range(len(s) - total_len + 1):
            tmp_str = s[i : i + total_len]
            tmp_list = []
            for j in range(0, total_len, word_len):
                w = tmp_str[j: j + word_len]
                tmp_list.append(w)
            if Counter(tmp_list) == counter:
                ans.append(i)
        return ans  
        
