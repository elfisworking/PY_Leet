# 913. 猫和老鼠
# https://leetcode-cn.com/problems/cat-and-mouse/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 913.py
@Time : 2022/01/04 10:22:54
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Hard
'''

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[[-1] * (n * 2) for _ in range(n)] for _ in range(n)]

        def getResult(mouse: int, cat: int, turns: int) -> int:
            if turns == n * 2:
                return DRAW
            res = dp[mouse][cat][turns]
            if res != -1: # 已经有结果了 直接返回
                return res
            if mouse == 0:
                res = MOUSE_WIN
            elif cat == mouse:
                res = CAT_WIN
            else:
                res = getNextResult(mouse, cat, turns) # 否则移动
            dp[mouse][cat][turns] = res # 记录结果
            return res

        def getNextResult(mouse: int, cat: int, turns: int) -> int:
            curMove = mouse if turns % 2 == 0 else cat
            defaultRes = MOUSE_WIN if curMove != mouse else CAT_WIN # 默认结果为最坏结果（如果是老鼠移动，默认为猫获胜，否则为老鼠获胜）
            res = defaultRes
            for next in graph[curMove]:
                if curMove == cat and next == 0: # 猫不能走到洞里（0节点）
                    continue
                nextMouse = next if curMove == mouse else mouse # 当前为老鼠移动，则老鼠下一步等于next
                nextCat = next if curMove == cat else cat # 当前为猫移动，则猫下一步等于next
                nextRes = getResult(nextMouse, nextCat, turns + 1)
                if nextRes != defaultRes: # 如果不是最坏结果 （可能获胜可能平局）
                    res = nextRes
                    if res != DRAW:  # // 如果获胜，直接结束循环，返回结果
                        break
            return res

        return getResult(1, 2, 0)