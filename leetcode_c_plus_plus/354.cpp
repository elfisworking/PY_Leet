// 354. 俄罗斯套娃信封问题
// https://leetcode-cn.com/problems/russian-doll-envelopes/
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
@File : 354.cpp
@Time : 2021/12/29 14:36:43
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Hard
**/
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int num = envelopes.size();
        vector<int> dp(num, 1);
        sort(envelopes.begin(), envelopes.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0] || (a[0] == b[0] && a[1] > b[1] );
        });
        for(int i = 1; i < num; i++) {
            int tmp = 0;
            for(int j = i -1; j >= 0; j--) {
                if(envelopes[j][0] < envelopes[i][0] && envelopes[j][1] < envelopes[i][1]) {
                    tmp = max(tmp, dp[j]);
                }
            }
            dp[i] += tmp;
        }
        int ans = 0;
        for(auto i : dp) {
            ans = max(ans, i);
        }
        return ans;


    }
};

class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        if (envelopes.empty()) {
            return 0;
        }
        
        int n = envelopes.size();
        sort(envelopes.begin(), envelopes.end(), [](const auto& e1, const auto& e2) {
            return e1[0] < e2[0] || (e1[0] == e2[0] && e1[1] > e2[1]);
        });

        vector<int> f = {envelopes[0][1]};
        for (int i = 1; i < n; ++i) {
            if (int num = envelopes[i][1]; num > f.back()) {
                f.push_back(num);
            }
            else {
                auto it = lower_bound(f.begin(), f.end(), num);
                *it = num;
            }
        }
        return f.size();
    }
};