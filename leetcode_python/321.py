# 321. 拼接最大数
# https://leetcode-cn.com/problems/create-maximum-number/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 321.py
@Time : 2022/03/21 22:17:31
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        #数组选k位最大自然数
        def selectMax(nums,k):
            stack=[]
            remain=len(nums)-k #可以舍弃的元素个数
            for num in nums:
                while remain and stack and num>stack[-1]: #注意是while，只要还能丢，就一直丢掉小的
                    stack.pop()
                    remain-=1
                stack.append(num)
            return stack[:k] #单调栈可能超出k个，比如nums一直递减的情况
        #合并两个数组为最大自然数
        def merge(A,B):
            ans=[]
            while A or B:
                bigger=max(A,B) #python数组直接能按元素顺序比大小,利用了python特性，不然要新定义一个方法
                ans.append(bigger[0])
                bigger.pop(0) #A/B会跟着bigger变
            return ans
        #对所有可能的两数组长度组合遍历，寻找最大数组
        maxlist=[0]*k
        for i in range(k+1): #i可以是0或者k，换句话说：可以只用到一个数组
            if i<=len(nums1) and k-i<=len(nums2):
                maxlist=max(maxlist,merge(selectMax(nums1,i),selectMax(nums2,k-i))) #还是利用了python特性
        return maxlist