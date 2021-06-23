# 剑指 Offer 38. 字符串的排列
# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
from typing import List
class Solution:
    # dfs
    def permutation(self, s: str) -> List[str]:
        l = len(s)
        use = [False]*l
        s = list(s)
        s.sort()
        ans = []
        def dfs(height,s1):
            if height == l:
                ans.append(s1)
            for i in range(l):
                if  use[i] or (i>0 and not use[i-1] and s[i-1]==s[i]):
                    continue
                use[i] = True
                dfs(height+1,s1+s[i])
                use[i] = False
        dfs(0,"")
        return ans