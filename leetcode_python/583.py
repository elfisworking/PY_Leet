# 583. 两个字符串的删除操作
# https://leetcode-cn.com/problems/delete-operation-for-two-strings/
# 题目：最长公共字串 1143
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1) 
        l2 = len(word2)
        dp = [ [0]*(l2+1) for _ in range(l1+1)]
        for i in range(l1+1):
            dp[i][0] = 1
        for i in range(l2+1):
            dp[0][i] = 1
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-1] + 1)
        
        max_length = dp[l1][l2] - 1
        return l1 -max_length + l2 - max_length
s = Solution()
print(s.minDistance("sea","eat"))
