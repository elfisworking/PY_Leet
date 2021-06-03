# 347. 前 K 个高频元素
# https://leetcode-cn.com/problems/top-k-frequent-elements/
from typing import List
from collections import defaultdict
# map计数
# 寻找前k个  可以使用快速排序 或者大小堆
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        res = []
        for i in nums:
            counts[i] += 1
        counts = sorted(counts.items(),key=lambda k:k[1],reverse=True)
        for i in range(k):
            res.append(counts[i][0])
        return res
