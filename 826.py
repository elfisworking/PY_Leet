from typing import List
# 826. 安排工作以达到最大收益
# https://leetcode-cn.com/problems/most-profit-assigning-work/
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        d = zip(difficulty,profit)
        d= sorted(d,key=lambda x:x[1],reverse=True)
        difficulty , profit = zip(*d)
        worker.sort(reverse=True)

        l = len(worker)
        l2 = len(difficulty)
        ptr1 = 0
        ptr2 = 0
        res = 0
        while ptr1 < l and ptr2 < l2:
            if worker[ptr1] >= difficulty[ptr2]:
                res += profit[ptr2]
                ptr1 += 1
            else:
                ptr2 += 1
        return res