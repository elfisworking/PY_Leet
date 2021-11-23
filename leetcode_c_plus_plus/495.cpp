// 495. 提莫攻击
// https://leetcode-cn.com/problems/teemo-attacking/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
/**
@File : 495.cpp
@Time : 2021/11/10 22:19:52
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int ans = 0;
        for(int i = 1; i < timeSeries.size(); i++) {
            if(timeSeries[i - 1 ] + duration - 1 >= timeSeries[i]) {
                ans += timeSeries[i] - timeSeries[i - 1];
            } else {
                ans += duration;
            }
        }    
        return ans + duration;    

    }
};