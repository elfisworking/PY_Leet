# 438. 找到字符串中所有字母异位词
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
from typing import List
import collections
# 思路：滑动窗口 维护一个数量字典 每一滑动 移动改变计数器
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #滑动窗口
        m = len(p)
        n = len(s)
        ans = []
        if m > n:
            return ans
        
        dp = 0

        time_1 = {i:0 for i in p}
        time_2 = time_1.copy()
        for i in p:
            time_1[i] += 1
        
        
        for j in range(m):
            tmp = time_2.get(s[j], -1)
            if tmp >= 0:
                time_2[s[j]] += 1
                if tmp < time_1[s[j]]:
                    dp += 1

        if dp == m:
            ans.append(0)
        for j in range(1, n - m + 1):
            tmp = time_2.get(s[m + j - 1], -1)
            if tmp >= 0:
                time_2[s[m + j - 1]] += 1
                if tmp < time_1[s[m + j - 1]]:
                    dp += 1
            
            tmp = time_2.get(s[j - 1], -1)
            if tmp >= 0:
                time_2[s[j - 1]] -= 1
                if tmp <= time_1[s[j - 1]]:
                    dp -= 1
            
            if dp == m:
                ans.append(j)
        
        return ans
        
        