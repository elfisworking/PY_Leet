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
        
# 2021.11.28
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        l2 = len(s)
        if l2 < l:
            return []
        p = list(p)
        p.sort()
        p = "".join(p)
        ans = []
        for i in range(l2 - l + 1):
            tmp = s[i:i + l]
            tmp = list(tmp)
            tmp.sort() 
            if "".join(tmp) == p:
                ans.append(i)
        return ans
        
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        l2 = len(s)
        if l2 < l:
            return []
        a = [0] * 26
        b = [0] * 26
        for i in p:
            a[ord(i) - ord("a")] += 1
        for i in range(l - 1):
            b[ord(s[i]) - ord("a")] += 1
        right = l -1 
        left = 0
        ans = []
        while right < l2:
            b[ord(s[right]) - ord("a")] += 1
            if a == b:
                ans.append(left)
            b[ord(s[left]) - ord("a")] -= 1
            left += 1
            right += 1

        return ans

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1

        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - 97] == 1:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i]) - 97] -= 1

            if count[ord(s[i + p_len]) - 97] == -1:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1
            
            if differ == 0:
                ans.append(i + 1)

        return ans
