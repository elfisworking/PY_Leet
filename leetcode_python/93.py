# 93. 复原 IP 地址
# https://leetcode-cn.com/problems/restore-ip-addresses/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 93.py
@Time : 2022/01/25 19:01:11
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Medium
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        SEG_COUNT = 4
        ans = []
        segments = [0] * SEG_COUNT
        def dfs(segId:int, segStart):
            if segId == SEG_COUNT:
                if segStart == len(s):
                    ipAddr = ".".join(str(seg) for seg in segments)
                    ans.append(ipAddr)
                return 
            if segStart == len(s):
                return 
            if s[segStart] == "0":
                segments[segId] = 0
                dfs(segId + 1, segStart + 1)
            addr = 0
            for segEnd in range(segStart, len(s)):
                addr = addr * 10 + (ord(s[segEnd]) - ord("0"))
                if 0 < addr <= 0xFF:
                    segments[segId] = addr
                    dfs(segId + 1, segEnd + 1)
                else:
                    break
        dfs(0, 0)
        return ans