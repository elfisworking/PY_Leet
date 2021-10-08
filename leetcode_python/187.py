# 187. 重复的DNA序列
# https://leetcode-cn.com/problems/repeated-dna-sequences/
from typing import List
from collections import defaultdict
L = 10
bin = {"A": 0, "C": 1, "G": 2, "T": 3}
class Solution:
    # def findRepeatedDnaSequences(self, s: str) -> List[str]:
    #     dic = defaultdict(int)
    #     for i in range(len(s)-9):
    #         dic[s[i:i+10]] += 1
    #     res = []
    #     for k ,v in dic.items():
    #         if v >= 2:
    #             res.append(k)
    #     return res
    # 2021.10.8
    # def findRepeatedDnaSequences(self, s: str) -> List[str]:
    #     if not s or len(s) < 10:
    #         return []
    #     h = defaultdict(int)
    #     left, right = 0, 10
    #     while right <= len(s):
    #         tmp = s[left:right]
    #         h[tmp] += 1
    #         left += 1
    #         right += 1
        
    #     ans = []
    #     for k, v in h.items():
    #         if v > 1:
    #             ans.append(k)
        
    #     return ans
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= L:
            return []
        ans = []
        x = 0
        for ch in s[:L - 1]:
            x = (x << 2) | bin[ch]
        
        cnt = defaultdict(int)
        for i in range(n - L + 1):
            x = (( x << 2) | bin[s[i + L -1]]) & ((1 << (L * 2)) - 1)
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i : i + L])
        return ans


