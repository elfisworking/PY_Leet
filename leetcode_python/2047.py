# 2047. 句子中的有效单词数
# https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence/submissions/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2047.py
@Time : 2022/01/27 15:06:14
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
'''
class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(s: str) -> bool:
            hasHyphens = False
            for i, ch in enumerate(s):
                if ch.isdigit() or ch in "!.," and i < len(s) - 1:
                    return False
                if ch == '-':
                    if hasHyphens or i == 0 or i == len(s) - 1 or not s[i - 1].islower() or not s[i + 1].islower():
                        return False
                    hasHyphens = True
            return True

        return sum(valid(s) for s in sentence.split())
