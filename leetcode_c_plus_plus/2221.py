# 2221. 数组的三角和
# https://leetcode-cn.com/problems/find-triangular-sum-of-an-array/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
from functools import lru_cache
import heapq
'''
@File : 2221.py
@Time : 2022/04/19 22:27:28
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Solution {
public:
    int triangularSum(vector<int>& nums) {
        queue<int> q;
        for(int i = 0; i < nums.size(); i++) {
            q.push(nums[i]);
        }
        int l = q.size();
        while(!q.empty() && q.size() > 1) {
            for(int i = 0; i < l - 1; i++) {
                auto a = q.front();
                q.pop();
                auto b = q.front();
                q.push((a + b) % 10);
            }
            q.pop();
            l = q.size();
            // printf("%d", l);
        }
        return q.front();
    }
};