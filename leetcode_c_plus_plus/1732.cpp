// 1732. 找到最高海拔
// https://leetcode-cn.com/problems/find-the-highest-altitude/
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
@File : 1732.cpp
@Time : 2022/03/28 22:57:44
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int curr = 0;
        int ans = 0;
        for(auto x : gain) {
            curr += x;
            ans = max(ans, curr);
        }
        return ans;
    }
};