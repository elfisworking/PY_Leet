// 539. 最小时间差
// https://leetcode-cn.com/problems/minimum-time-difference/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : 539.cpp
@Time : 2022/01/18 22:16:06
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
**/
class Solution {
public:
    int getMin(string& time) {
        return (int(time[0] - '0') * 10 + int(time[1] - '0')) * 60 + int(time[3] - '0') * 10 + int(time[4] - '0');
    }
    int findMinDifference(vector<string>& timePoints) {
        if(timePoints.size() > 1440) return 0; // 抽屉原理的运用 超过1440 = 24 * 60 必然有一个重复的
        sort(timePoints.begin(), timePoints.end());
        int pre_time = getMin(timePoints[0]);
        int t0_time = pre_time;
        int ans = INT_MAX;
        for(int i = 1; i < timePoints.size(); i++) {
            int cur = getMin(timePoints[i]);
            ans = min(ans, cur - pre_time);
            pre_time = cur;
        }
        ans = min(ans, t0_time + 1440 - pre_time);
        return ans;
    }
};