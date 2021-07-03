# 451. 根据字符出现频率排序
# https://leetcode-cn.com/problems/sort-characters-by-frequency/
from typing import List
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        h = defaultdict(int)
        for i in s:
            h[i] += 1
        s = sorted(h.items(),key = lambda x:x[1],reverse= True)
        ans = []
        for val in  s:
            for _ in range(val[1]):
                ans.append(val[0])
        return "".join(ans)