# 剑指 Offer 19. 正则表达式匹配
# https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/
# 没有想起来
# 一开始使用状态机的写法但是根本没有办法处理
# 太他妈的恶心了
# 这里官方使用了dp的写法 需要好好的想想
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m , n = len(s) , len(p)
        def matches(i,j):
            if i == 0:
                return False
            if p[j-1] == ".":
                return True
            return s[i-1] == p[j-1]
        f = [[False for _ in range(n+1)] for _ in range(m+1)]
        f[0][0] = True
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1] == "*":
                    f[i][j] |= f[i][j-2]
                    if matches(i,j-1):
                        f[i][j] |= f[i-1][j]
                else:
                    if matches(i,j):
                        f[i][j] |= f[i-1][j-1]
        
        return f[m][n]
