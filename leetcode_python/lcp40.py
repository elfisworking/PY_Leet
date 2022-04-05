# LCP 40. 心算挑战
# https://leetcode-cn.com/problems/uOAnQW/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : lcp40.py
@Time : 2022/04/04 21:21:39
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        odd, even = [0], [0]  # 前缀和数组（向右偏移一个单位）
        for card in cards:
            if card & 1:
                odd.append(odd[-1] + card)
            else:
                even.append(even[-1] + card)
        
        # 枚举奇数个数
        ans = 0
        for k in range(0, len(odd), 2):  # 原序列中取偶数个奇数
            if 0 <= cnt - k < len(even):  # 原序列中取足够个偶数
                ans = max(ans, odd[k] + even[cnt-k])  # 排序后前面的数字是最大的，O(1)得到它们的和
        return ans
