#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 677.py
@Time : 2021/11/14 15:47:28
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : 一开始写错了，没有读清题目，使用字典树的思路是正确的
'''
# class MapSum:

#     def __init__(self):
#         self.child = defaultdict(MapSum)
#         self.is_end = False
#         self.val = 0
#         self.value = 0

#     def insert(self, key: str, val: int) -> None:
#         node = self
#         for char in key:
#             if char not in node.child:
#                 new_node = MapSum()
#                 new_node.val += val
#                 new_node.value += val
#                 node.child[char] = new_node
#                 node = new_node
#             else:
#                 node = node.child[char]
#                 if node.is_end:
#                     node.val = node.val - node.value + val
#                     node.value = val
#                 else:
#                     node.val += val
#         node.is_end = True
    
#     def sum(self, prefix: str):
#         node = self
#         if not node.child:
#             return 0
#         for char in prefix:
#             if char in node.child:
#                 node = node.child[char]
#         return node.val


class TrieNode:
    def __init__(self):
        self.val = 0
        self.next = [None for _ in range(26)]

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val
        node = self.root
        for c in key:
            if node.next[ord(c) - ord('a')] is None:
                node.next[ord(c) - ord('a')] = TrieNode()
            node = node.next[ord(c) - ord('a')]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if node.next[ord(c) - ord('a')] is None:
                return 0            
            node = node.next[ord(c) - ord('a')]
        return node.val


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("aa", 3)
param_2 = obj.sum("a")
obj.insert("aa", 2)
param_3 = obj.sum("aa")
print(param_3)
print(obj.sum("a"))