# 青蛙过河
# https://leetcode-cn.com/problems/frog-jump/
# 腾讯微信实习面试题
import bisect
from typing import List
import functools
class Solution:
    # 第一次运行超时了
    # 为什么??
    def canCross(self, stones: List[int]) -> bool:
        l = len(stones)
        rec = [ [0 for _ in range(l)] for _ in range(l)]
        def dfs(i,lastDis):
            if i == l-1:
                return True
            if rec[i][lastDis] != 0:
                return rec[i][lastDis]
            for curDis in range(lastDis-1,lastDis+2):
                if curDis > 0:
                    j = bisect.bisect_left(stones,curDis+stones[i])
                    if j < l and (stones[j] == stones[i]+curDis) and dfs(j,curDis):
                        rec[i][lastDis] = True
                        return rec[i][lastDis]
            rec[i][lastDis] = False
            return rec[i][lastDis]
        return dfs(0,0)
    
    def canCross_others(self, stones: List[int]) -> bool:
        """
        f(i, j)上一步跳了 j 步，来到当前的 i 位置，基于此，能否最后抵达终点。
        """
        @functools.lru_cache(None)
        def f(i, j):
            if i == len(stones) - 1: return True
            if j == 0: steps = [1]
            elif j == 1: steps = [1, 2]
            else: steps = [j - 1, j, j + 1]
            for step in steps:
                idx = bisect.bisect_left(stones, stones[i] + step)
                if idx < len(stones) and (stones[idx] == stones[i] + step) and f(idx, step):
                    return True
            return False
        return f(0, 0)
    
    def canCross(self, stones: List[int]) -> bool:
        @functools.lru_cache(None)
        def bfs(idx, k):
            if k == 0:
                return False
            if idx == n - 1:
                return True
            for i in range(idx + 1, n):
                diff = stones[i] - stones[idx]
                if k - 1 <= diff <= k + 1 and bfs(i, diff):
                    return True
                elif diff > k + 1:
                    break
            return False

        n = len(stones)
        if stones[1] != 1:
            return False
        return bfs(1, 1)
s = Solution()
print(s.canCross([0,1,2,3,4,8,9,11]))