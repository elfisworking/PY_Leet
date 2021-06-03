from typing import List
import bisect
class Solution:
    # 使用动态规划的方法 一维数组 会有超时的风险 O(n^2)的时间复杂度
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda enve:(enve[0],-enve[1]))
        l = len(envelopes)
        dp = [ 1 for _ in range(l)]
        for a in range(l):
            for b in range(a):
                if  envelopes[a][1]>envelopes[b][1] :
                    dp[a] = max(dp[b]+1,dp[a])
        return max(dp)

        # 采用二分搜索进行优化的 dp算法
    def maxEnvelopes_offical(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        f = [envelopes[0][1]]
        for i in range(1, n):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num
        
        return len(f)    
s = Solution()
print(s.maxEnvelopes_offical([[5,4],[6,4],[6,7],[2,3]]))