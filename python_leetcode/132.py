class Solution:
    # 采用深度搜索的方法会导致超时 需要改进
    def minCut(self, s: str) -> int:
        l = len(s)
        f = [[True]*l for _ in range(l)]
        for i in range(l-1,-1,-1):
            for j in range(i+1,l):
                f[i][j] = (s[i]==s[j]) and f[i+1][j-1]
        ans = l 

        def dfs(i:int,res):
            if i == l:
                nonlocal ans
                ans = min(ans,res-1)
            for j in range(i,l):
                if f[i][j]:
                    res += 1
                    dfs(j+1,res)
                    res -= 1
        
        dfs(0,0)
        return ans
    def minCut_offical(self, s: str) -> int:
        l = len(s)
        f = [[True]*l for _ in range(l)]
        for i in range(l-1,-1,-1):
            for j in range(i+1,l):
                f[i][j] = (s[i]==s[j]) and f[i+1][j-1]
        
        g = [float("inf")]*l
        print(g)
        for i in range(l):
            if f[0][i] :
                g[i] = 0
            else:
                for j in range(i):
                    if f[j+1][i]:
                        g[i] = min(g[i],g[j]+1)

        return g[l-1] 
        


s = Solution()
print(s.minCut_offical("abbba"))