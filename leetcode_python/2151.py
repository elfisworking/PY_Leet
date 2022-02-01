#
#
from curses.ascii import SO
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2151.py
@Time : 2022/01/27 12:59:15
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maximumGood(self, s: List[List[int]]) -> int:
        ans = 0
        l = len(s)
        
        for i in range((1 << l) - 1, -1 , -1):
            # if ans > 0:
            #     break
            goods = set()
            bads = set()
            flag = True
            good_num = 0
            for j in range(l):
                if not flag:
                    break
                idx = i & (1 << j)
                if idx == 0 and j in goods:
                    flag = False
                    break
                elif idx == 0:
                    bads.add(j)
                    continue
                if idx >= 1 and j in bads:
                        flag = False
                        break
                elif idx == 1:
                    goods.add(j)
                    good_num += 1
                for k in range(l):
                    if s[j][k] == 0 and k in goods:
                        flag = False
                        break
                    elif s[j][k] == 0:
                        bads.add(k)
                    if s[j][k] == 1 and k in bads:
                        flag = False
                        break
                    elif s[j][k] == 1:
                        goods.add(k)
            if flag:
                print(i, good_num)
                ans = max(ans, good_num)
        return ans
                
s = Solution()
print(s.maximumGood([[2,1,2],[1,2,2],[2,0,2]]))

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        ans = 0
        for mask in range(1, 1 << n):
            def check() -> bool:
                for i in range(n):
                    for j in range(n):
                        if i == j:
                            continue
                        if statements[i][j] == 0:
                            if mask & (1 << i) and mask & (1 << j):
                                return False
                        elif statements[i][j] == 1:
                            if mask & (1 << i) and not mask & (1 << j):
                                return False
                return True
            
            if check():
                ans = max(ans, bin(mask).count("1"))
        return ans

class Solution:
    def maximumGood(self, s: List[List[int]]) -> int:
        l = len(s)
        ans = 0
        for i in range(0, 1 << l):
            def check():
                for j in range(l):
                    for k in range(l):
                        if s[j][k] == 0:
                            if i & (1 << j) and i & (1 << k):
                                return False
                        if s[j][k] == 1:
                            if i & (1 << j) and not i & (1 << k):
                                return False
                return True
            if check():
                ans = max(ans, bin(i).count("1")) 
        return ans
