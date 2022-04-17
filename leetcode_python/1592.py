# 1592. 重新排列单词间的空间
# https://leetcode-cn.com/problems/rearrange-spaces-between-words/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 1592.py
@Time : 2022/04/07 20:16:08
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_num = 0
        word_num = 0
        flag = True
        for i in text:
            if i == " ":
                space_num += 1
                flag = True
            else:
                if flag:
                    word_num += 1
                    flag = False
        
        text = text.strip().split()
        mid_space_num = space_num // (word_num - 1) if word_num > 1 else 0
        addion_space_num = space_num % (word_num - 1) if word_num > 1 else space_num
        mid_space = ' ' * mid_space_num
        ans = mid_space.join(text) + ' ' * addion_space_num
        return ans