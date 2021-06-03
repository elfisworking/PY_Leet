# 91. 解码方法
# https://leetcode-cn.com/problems/decode-ways/
class Solution:
    # 递归方法超时  需要改进 暴力方法不可取
    def numDecodingsUsingRecurion(self, s: str) -> int:
        l = len(s)
        def get_num(i):
            if i >= l:
                return 1
            m = 0
            if 1<=int(s[i])<=9:
                m += get_num(i+1)
            if i+1 < l and int(s[i])==1 and 0<=int(s[i+1])<=9:
                m += get_num(i+2)
            elif i+1 < l and int(s[i])==2 and 0<=int(s[i+1])<=6:
                m += get_num(i+2)
            return m 
        return get_num(0)
        
    # 跟爬楼梯很像  如果将其抽象的话 
    def numDecodings(self, s: str) -> int:
        l = len(s)
        s = " "+s
        dp = [0]*(l+1)
        dp[0] = 1
        for i in range(i,l+1):
            a = ord(s[i]) - ord('0')
            b = ( ord(s[i - 1]) - ord('0') ) * 10 + ord(s[i]) - ord('0')
            if 1 <= a <= 9:
                dp[i] = dp[i-1]
            if 10<=b<=26:
                dp[i] +=dp[i-2]
        return dp[l] 


            
s = Solution()
print(s.numDecodings("1223262321327881239"))