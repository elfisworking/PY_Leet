# 520. 检测大写字母
# https://leetcode-cn.com/problems/detect-capital/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 520.py
@Time : 2021/11/14 15:10:47
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        flag =True
        for i in range(len(word)):
            if flag and word[i].isupper():
                continue
            else:
                if not flag:
                    if word[i].isupper():
                        return False
                elif i <= 1:
                    flag = False
                else:
                    return False 
        return True