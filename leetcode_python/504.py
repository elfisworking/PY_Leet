# 504. 七进制数
# https://leetcode-cn.com/problems/base-7/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 504.py
@Time : 2022/03/07 22:59:40
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = []
        flag = False
        if num < 0:
            flag = True
            num = abs(num)
        if num == 0:
            return "0"    
        while num > 0:
            bit = num % 7
            num = num // 7
            ans.append(str(bit))
        if flag:
            ans.append("-")
        ans.reverse()
        return "".join(ans)