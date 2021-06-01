# 763. 划分字母区间
# https://leetcode-cn.com/problems/partition-labels/
from typing import List
from collections import Counter , defaultdict
class Solution:
    # 10% 
    def partitionLabels_loop(self, s: str) -> List[int]:
        counter = Counter(s)
        left , right = 0 ,0
        l = len(s)
        d = defaultdict(int)
        res = [] 
        def check():
            for key in d.keys():
                if d[key] != counter[key]:
                    return False
            return True
        while right < l:
            d[s[right]] += 1
            if check():
                res.append(right-left+1)
                left = right + 1
                d.clear()
            right += 1
        return res

    def partitionLabels(self, s: str) -> List[int]:
        last = [0]*26
        for i , ch in enumerate(s):
            last[ord(ch)-ord('a')] = i
        
        partition = list()
        start = end = 0
        for i , ch in enumerate(s):
            end = max(end,last[ord(ch)-ord("a")])
            if i == end:
                partition.append(end-start+1)
                start = end + 1
        return partition