# 砖墙
# https://leetcode-cn.com/problems/brick-wall/
from collections import defaultdict
from typing import List
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height  = len(wall)
        wall_dict =defaultdict(int)
        wall_dict[0] = 0
        for row in  wall:
            b = 0
            for a in range(len(row)-1):
                b += row[a]
                wall_dict[b] = wall_dict[b]+1

        return height-max(wall_dict.values())