# 384. 打乱数组
# https://leetcode-cn.com/problems/shuffle-an-array/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
import random
'''
@File : 384.py
@Time : 2021/11/23 22:38:33
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
'''

## 投机取巧
class Solution_1:

    def __init__(self, nums: List[int]):
        self.origin = [i for i in nums]

    def reset(self) -> List[int]:
        return self.origin

    def shuffle(self) -> List[int]:
        shuf = [i for i in self.origin]
        random.shuffle(shuf)
        return shuf


# 洗牌算法
class Solution:

    def __init__(self, nums: List[int]):
        self.origin = [i for i in nums]

    def reset(self) -> List[int]:
        return self.origin

    def shuffle(self) -> List[int]:
        shuf = [i for i in self.origin]
        for i in range(len(shuf)):
            j = random.randrange(i, len(shuf))
            shuf[i], shuf[j] = shuf[j], shuf[i]
        return shuf


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# 洗牌算法
# https://zhuanlan.zhihu.com/p/107901559
# https://www.legr4ndk.top/2021/03/13/KnuthShuffle/index.html

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums