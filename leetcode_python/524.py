# 524. 通过删除字母匹配到字典里最长单词
# https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/
from typing import List
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for t in dictionary:
            i = j = 0
            while i < len(t) and j < len(s):
                if t[i] == s[j]:
                    i += 1
                j += 1
            if i == len(t):
                return t
        return ""