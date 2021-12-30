# 846. 一手顺子
# https://leetcode-cn.com/problems/hand-of-straights/
from typing import List
from collections import defaultdict
from collections import deque
from collections import Counter
from math import inf
import bisect
import heapq
'''
@File : 846.py
@Time : 2021/12/30 10:13:32
@Author : YuMin Zhang
@State : Indepeedent 
@Thinking :
@Tag : Medium
'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l = len(hand)
        if l % groupSize != 0: return False
        counter = Counter(hand)
        while counter:
            keys = counter.keys() 
            minkey = min(keys)
            maxkey = max(keys)
            for i in range(groupSize):
                if minkey in counter:
                    counter[minkey] -= 1
                else:
                    return False
                if counter[minkey] == 0:
                    del counter[minkey]
                minkey += 1
            if not counter: return True
            for i in range(groupSize):
                if maxkey in counter:
                    counter[maxkey] -= 1
                else:
                    return False
                if counter[maxkey] == 0:
                    del counter[maxkey]
                maxkey -= 1
        return True

# 官方的时间复杂度更低一点, 但是思想基本都是对的， 都是贪心的思想
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False
        hand.sort()
        cnt = Counter(hand)
        for x in hand:
            if cnt[x] == 0:
                continue
            for num in range(x, x + groupSize):
                if cnt[num] == 0:
                    return False
                cnt[num] -= 1
        return True
s = Solution()
print(s.isNStraightHand([1,2,3,4,5,6], 3))