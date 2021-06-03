from typing import List
class Solution:
    def partition(self,s:str) ->List[List[str]]:
        n = len(s)
        f = [[True]*n for _ in range(n)]
        # 合适的扫描顺序 避免f[i+1][j-1]不存在的情况
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                f[i][j] = (s[i]==s[j]) and f[i+1][j-1]

        res = list()
        ans = list()

        def dfs(i:int):
            if i == n:
                res.append(ans[:])
                return

            for j in range(i,n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j+1)
                    ans.pop()

        dfs(0)
        return res     