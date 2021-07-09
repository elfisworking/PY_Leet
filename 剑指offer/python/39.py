# 剑指 Offer 39. 数组中出现次数超过一半的数字
# https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 39.py
@Time : 2021/07/09 13:42:55
@Author : YuMin Zhang
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔算法 时间 O(n) 空间O(1) 
        candidate = -1
        cnt = 0
        for i in nums:
            if cnt == 0:
                candidate = i
                cnt = 1
            else:
                if candidate == i:
                    cnt += 1
                else:
                    cnt -= 1
        if cnt == 0:
            return -1
        cnt = 0
        for i in nums:
            if i == candidate:
                cnt += 1
        return candidate if cnt > len(nums)//2 else -1