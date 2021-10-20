# 211. 添加与搜索单词 - 数据结构设计
# https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 211.py
@Time : 2021/10/19 23:08:31
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
# class WordDictionary:

#     def __init__(self):
#         self.d = defaultdict(list)


#     def addWord(self, word: str) -> None:
#         self.d[len(word)].append(word)
#     查找进行了优化
#     def search(self, word: str) -> bool:
#         l = len(word)
#         words = self.d[l]
#         for w in words:
#             flag = True
#             for i in range(l):
#                 if word[i] != "." and word[i] != w[i]:
#                     flag = False
#                     break
#             if flag:
#                 return True
#         return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# 字典树
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True


class WordDictionary:
    def __init__(self):
        self.trieRoot = TrieNode()

    def addWord(self, word: str) -> None:
        self.trieRoot.insert(word)

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.isEnd
            ch = word[index]
            if ch != '.':
                child = node.children[ord(ch) - ord('a')]
                if child is not None and dfs(index + 1, child):
                    return True
            else:
                for child in node.children:
                    if child is not None and dfs(index + 1, child):
                        return True
            return False

        return dfs(0, self.trieRoot)
