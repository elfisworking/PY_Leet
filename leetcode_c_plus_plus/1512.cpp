// 1512. 好数对的数目
// https://leetcode-cn.com/problems/number-of-good-pairs/
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
@File : 1512.cpp
@Time : 2022/03/30 23:03:41
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int, int> map;
        int ans = 0;
        for(auto x : nums) {
            if(map.count(x)) {
                ans += map[x];
                map[x]++;
            } else {
                map[x] = 1;
            }
        }
        return ans;
    }
};