'''
丑数 II
https://leetcode-cn.com/problems/ugly-number-ii/
'''
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        fac = [2,3,5]
        seen = {1}
        heap = [1]
        for _ in range(n-1):
            curr = heapq.heappop(heap)
            for f in fac:
                val = curr*f 
                if val not in seen:
                    seen.add(val)
                    heapq.heappush(heap,val)
        return heapq.heappop(heap)
    
    # 采用了动态规划的方法 暂时无法理解
    def nthUglyNumber_dp(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        
        return dp[n]