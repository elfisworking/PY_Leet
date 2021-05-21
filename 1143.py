# 1143. 最长公共子序列
# https://leetcode-cn.com/problems/longest-common-subsequence/
# 可以查看最长公共子序列的变体题：
# 1035. 不相交的线
# https://leetcode-cn.com/problems/uncrossed-lines/
# 不相交的线可以看作的最长的公共子序列
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0 for _ in range(l1+1)] for _ in range(l2+1)]
        for a in range(1,l2+1):
            for b in range(1,l1+1):
                if text2[a-1] == text1[b-1]:
                    dp[a][b] = dp[a-1][b-1] + 1
                else:
                    dp[a][b] = max(dp[a-1][b],dp[a][b-1])
        return dp[l2][l1]

        