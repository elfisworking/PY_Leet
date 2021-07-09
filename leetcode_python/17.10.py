# 面试题 17.10. 主要元素
# https://leetcode-cn.com/problems/find-majority-element-lcci/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import heapq
'''
@File : 17.10.py
@Time : 2021/07/09 10:44:01
@Author : YuMin Zhang
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        考察摩尔算法 时间复杂度O(n),空间复杂度O(1)
        如果使用哈希表，那么时间复杂度O(n),空间复杂度O(n)
        '''
        l = len(nums)
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
        counter = 0
        for i in nums:
            if i == candidate:
                counter +=1
        return candidate if counter > l//2 else -1
s = Solution()
print(s.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))