# 2049. 统计最高分的节点数目
# https://leetcode-cn.com/problems/count-nodes-with-the-highest-score/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2049.py
@Time : 2022/03/11 22:28:21
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        ans  = 0
        l = len(parents)
        nums = [0] * l
        tree = defaultdict(list)
        for i, val in enumerate(parents):
            tree[val].append(i)
        def dfs(node):
            if node not in tree:
                nums[node] = 1
                return 1
            num = 1
            for child in tree[node]:
                num += dfs(child)
            nums[node] = num
            return num 
        dfs(0)
        print(nums)
        max_value = 0
        for i in range(l):
            par_num = 1
            if parents[i] != -1:
                par_num = nums[0] - nums[i]
            child_num = 1 
            for child in tree[i]:
                child_num *= nums[child]
            curr_node = child_num * par_num
            if curr_node > max_value:
                ans = 1
                max_value = curr_node
            elif curr_node == max_value:
                ans += 1
        return ans
s = Solution()
print(s.countHighestScoreNodes([-1,2,0]))