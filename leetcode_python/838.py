#
#
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 838.py
@Time : 2022/02/21 21:20:46
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        length = len(dominoes)
        ans = ["."] * length
        if length == 1:
            return dominoes
        left = 0
        while left < length:
            
            if dominoes[left] != ".":
                ans[left] = dominoes[left]
                left += 1
            else:
                right = left
                while right < length and dominoes[right] == ".":
                    right += 1
                l = left
                left = right
                r = right - 1
                if l == 0:
                    if right <  length and dominoes[right] == "L":
                        for i in range(l, right):
                            ans[i] = "L"
                elif right == length:
                    if l > 0 and dominoes[l - 1] == "R":
                        for i in range(l, right):
                            ans[i] = "R" 
                else:
                    if dominoes[l - 1] == dominoes[right]:
                        for i in range(l, right):
                            ans[i] = dominoes[right]
                    if dominoes[l - 1] == "R" and dominoes[right] == "L":
                        while l < r:
                            ans[l] = "R"
                            ans[r] = "L"
                            l  += 1
                            r -= 1           
        return "".join(ans)
s = Solution()
print(s.pushDominoes("R.......L.R........."))