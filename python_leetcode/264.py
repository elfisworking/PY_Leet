'''
丑数 II
https://leetcode-cn.com/problems/ugly-number-ii/
'''
import heapq
class Solution:
    # 采用最小堆的方法
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
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # dp = [1]
        # p2 = p3 = p5 = 0

        # for i in range(1, n ):
        #     num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
        #     dp.append(min(num2, num3, num5))
        #     if dp[i] == num2:
        #         p2 += 1
        #     if dp[i] == num3:
        #         p3 += 1
        #     if dp[i] == num5:
        #         p5 += 1
        res = [1]
        p2, p3 , p5 = 0,0,0
        for i in range(1,n):
            val = min(res[p2]*2,res[p3]*3,res[p5]*5)
            res.append(val)
            print(res,p2,p3,p5)
            if val == res[p2]*2:
                p2 += 1
            if val == res[p3]*3:
                p3 += 1
            if val == res[p5]*5:
                p5 += 1
        return res[n-1]
        
        # return dp[n-1]
s = Solution()
print(s.nthUglyNumber_dp(10))