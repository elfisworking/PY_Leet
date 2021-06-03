# 179 最大数
# https://leetcode-cn.com/problems/largest-number/
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        l = [str(i) for i in nums]
        # 用一个冒泡来排序
        for a in range(1,len(l)):
            for i in range(0,len(l)-a):
                if int(l[i]+l[i+1])>int(l[i+1]+l[i]):
                    l[i],l[i+1] = l[i+1],l[i]
        res =""
        for i in range(len(l)-1,-1,-1):
            res += l[i]
        # 避免[0,0]的情况
        res = str(int(res))
        return res