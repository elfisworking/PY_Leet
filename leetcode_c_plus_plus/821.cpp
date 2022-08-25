// 821. 字符的最短距离
// https://leetcode-cn.com/problems/shortest-distance-to-a-character/
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
@File : 821.cpp
@Time : 2022/04/19 22:13:50
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        int n = s.size();
        vector<int> ans(n);
        for(int i = 0, idx = -n; i < n; i++) {
            if(s[i] == c) {
                idx = i;
            }
            ans[i] = i - idx;
        }
        for(int i = n - 1, idx = 2 * n; i >=0; i--) {
            if(s[i] == c) {
                idx = i;
            }
            ans[i] = min(ans[i], idx - i);
        }
        return ans;
    }
};
