# 剑指 Offer 46. 把数字翻译成字符串
# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 46.py
@Time : 2021/07/12 10:24:55
@Author : YuMin Zhang
'''
class Solution:
    def translateNum_dfs(self, num: int) -> int:
        # 使用深度搜索的方法
        ans = 0
        def dfs(l,num,length):
            nonlocal ans
            if l >= length:
                ans += 1
                return 
            if l<length-1 and num[l] != "0" and int(num[l:l+2])<=25:
                dfs(l + 2,num,length)
            dfs(l+1,num,length)
        num = str(num)
        dfs(0,num,len(num))
        return ans
    
    def translateNum_dp(self, num: int) -> int:
        num = str(num)
        l = len(num)
        dp = [1]*l
        for i in range(1,l):
            dp[i] = dp[i-1]
            if  num[i-1] != "0" and  int(num[i-1,i+1]) < 26:
                dp[i] += dp[i-2]
        return dp[l-1]