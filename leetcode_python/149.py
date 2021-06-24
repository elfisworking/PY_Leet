# 149. 直线上最多的点数
# https://leetcode-cn.com/problems/max-points-on-a-line/
from typing import List
from collections import defaultdict
class Solution:
    # 这个方法思路是对的 但是斜率的表示可能会出问题 同时没有考虑到 无穷的情况
    def maxPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        d = defaultdict(set)
        for i in range(l):
            for j in range(i+1,l):
                x = points[i][0]-points[j][0]
                if x == 0:
                    continue
                k = (points[i][1]-points[j][1])/ x
                d[k].add((points[i][0],points[i][1]))
                d[k].add((points[j][0],points[j][1]))
        a = d.values()
        a = sorted(a,key = lambda i:len(i),reverse=True)
        return len(a[0])
s = Solution()
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))