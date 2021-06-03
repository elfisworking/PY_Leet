# 664. 奇怪的打印机
# https://leetcode-cn.com/problems/strange-printer/
# 输入：s = "aba"
# 输出：2
# 解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
class Solution:
    # 应该使用什么方法
    # dp 
    # 转移方程是什么
    # dp[i][j] = 
    def strangePrinter(self, s: str) -> int:
        res = 0
        l = len(s)
        dp = [[0 for _ in range(l+1) ]for _ in range(l+1)]
        for a in range(1,l+1):
            for b in range(l-a+1):
                r = a + b-1
                dp[b][r] = dp[b+1][r]+1
                for k in range(b+1,r+1):
                    if s[b] == s[k]:
                        dp[b][r] = min(dp[b][r],dp[b][k-1]+dp[k+1][r])
        
        return dp[0][l-1]

        return res
        