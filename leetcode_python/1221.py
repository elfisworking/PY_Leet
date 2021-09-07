# 1221. 分割平衡字符串
# https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # greedy algorithm
        L_counter = 0
        R_counter = 0
        l = len(s)
        res = 0
        for ch in s:
            if ch == "L":
                L_counter += 1
            elif ch == "R":
                R_counter += 1
            if R_counter == L_counter:
                R_counter = 0
                L_counter = 0
                res += 1
        return res
            