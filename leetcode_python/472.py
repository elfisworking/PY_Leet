# 472. 连接词
# https://leetcode-cn.com/problems/concatenated-words/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 472.py
@Time : 2021/12/28 10:23:56
@Author : YuMin Zhang
@State : Depedent 
@Thinking : 前缀树 和 DFS
@Tag : Hard
'''
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def dfs(self, word: str, start: int, vis: List[bool]) -> bool:
        if start == len(word):
            return True
        if vis[start]: # 记忆化搜索
            return False
        vis[start] = True
        node = self
        for i in range(start, len(word)):
            node = node.children[ord(word[i]) - ord('a')]
            if node is None:
                return False
            if node.isEnd and self.dfs(word, i + 1, vis):
                return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)

        ans = []
        root = Trie()
        for word in words:
            if word == "":
                continue
            if root.dfs(word, 0, [False] * len(word)):
                ans.append(word)
            else:
                root.insert(word)
        return ans

s = Solution()
print(s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
