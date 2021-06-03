import functools
# 1269. 停在原地的方案数
# https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # 直接递归超时 
        count = [0]
        def dfs(location,step,left,mid):
            if step == steps:
                print("当前的location是",location)
                if location == 0:
                    count[0] += 1
                return 
            if left > (steps-mid)//2:
                return 
            for i in range(3):
                if i == 1 and location+1 < arrLen:
                    print("当前执行的是 + 1")
                    dfs(location+1,step+1,left,mid)
                elif location > 0 and i == 2:
                    print("当前执行的是 - 1")
                    dfs(location-1,step+1,left+1,mid)
                elif i == 0:
                    print("当前执行的是 0")
                    dfs(location,step+1,left,mid+1)
        dfs(0,0,0,0)
        return count[0]

    def numWays_1(self, steps: int, arrLen: int) -> int:
        @functools.lru_cache(None)
        def dfs(pos,c):
            if c==steps and pos == 0:
                return 1
            if c==steps and pos!=0:
                return 0
            res = 0
            if pos==0:
                for i in [0,1]:
                    res+=dfs(pos+i,c+1)
            elif pos == arrLen-1:
                for i in [0,-1]:
                    res+=dfs(pos+i,c+1)
            else:
                for i in [-1,0,1]:
                    res+=dfs(pos+i,c+1)
            return res
        return dfs(0,0)%(10**9 + 7)
    def numWays_dp(self, steps: int, arrLen: int) -> int:
        maxCol = min(steps//2+1,arrLen-1)
        dp = [[0 for _ in range(maxCol+1)]for _ in range(steps+1)]
        dp[0][0] = 1
        for i in range(1,steps+1):
            for j in range(0,maxCol+1):
                if j==0:
                    dp[i][j] = (dp[i-1][j]+dp[i-1][j+1])%(10**9+7)
                elif j == maxCol:
                    dp[i][j]  = (dp[i-1][j]+dp[i-1][j-1])%(10**9+7)
                else:
                    dp[i][j] = ((dp[i-1][j] + dp[i-1][j-1])%1000000007 + dp[i-1][j+1])%1000000007
        return dp[steps][0]
s = Solution()
print(s.numWays_dp(3,2))