# 630. 课程表 III
# https://leetcode-cn.com/problems/course-schedule-iii/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 630.py
@Time : 2021/12/14 10:50:12
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : 单机作业调度问题
'''
# 错误
# class Solution:
#     def scheduleCourse(self, courses: List[List[int]]) -> int:
#         courses.sort(key=lambda x : x[1] x[0])
#         ans = 0
#         j = 0
#         for i in range(0, len(courses)):
#             if j + courses[i][0] <= courses[i][1]:
#                 j += courses[i][0]
#                 ans += 1
#         return ans

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])

        q = list()
        # 优先队列中所有课程的总时间
        total = 0

        for ti, di in courses:
            if total + ti <= di:
                total += ti
                # Python 默认是小根堆
                heapq.heappush(q, -ti)
            elif q and -q[0] > ti:
                total -= -q[0] - ti
                heapq.heappop(q)
                heapq.heappush(q, -ti)

        return len(q)