def longestPalindrome(s: str) -> str:
    s = '#'+'#'.join(s)+'#'
    MaxRight = 0
    pos = 0
    MaxLen = 0
    RL = [0]*len(s)
    for i in range(len(s)):
        if i < MaxRight:
            RL[i] = min(RL[2*pos],MaxRight-i)
        else:
            RL[i] = 1
        while i - RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
            RL[i] +=1
        if RL[i]+i-1 > MaxRight:
            MaxRight=RL[i]+i-1
        MaxLen = max(MaxLen,RL[i])
    return MaxLen-1
# 使用中心扩散方法    
def longestPalindrome_2(s):
    s="#".join(list(s))
    MaxLength=0
    length = len(s)
    for index in range(length):
        m = 0
        for i in range(0,min(index,length-index-1)+1):
            if i == 0 :
                if s[index] != "#":
                    m += 1
                    continue
            if s[index-i] == s[index+i]:
                    if s[index-i] != "#":
                        m +=2
            else:
                break
        if m > MaxLength:
            MaxLength = m
    return  MaxLength
        
# 使用动态规划dp
# dp[i:j]=dp[i-1:j-1]+2 if dp[i]==dp[j]
#             
def longestPalindrome_3(s):
    size = len(s)
    if size < 2:
        return s
    dp =[[False for _ in range(size)] for _ in range(size)]
    max_len = 1
    start = 0
    for i in range(size):
        dp[i][i] = True
    for j in range(1,size):
        for i in range(0,j):
            if s[i]==s[j]:
                if j-i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] =False
            if dp[i][j]:
                cur_len = j-i+1
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    return s[start:start+max_len]
            


class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]

print(longestPalindrome_3("bcvcbfbcvc"))
