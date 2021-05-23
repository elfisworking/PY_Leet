# 187. 重复的DNA序列
# https://leetcode-cn.com/problems/repeated-dna-sequences/
from typing import List
from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = defaultdict(int)
        for i in range(len(s)-9):
            dic[s[i:i+10]] += 1
        res = []
        for k ,v in dic.items():
            if v >= 2:
                res.append(k)
        return res


