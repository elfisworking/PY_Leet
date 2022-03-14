// 1601. 最多可达成的换楼请求数目
// https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests/
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
@File : 1601.cpp
@Time : 2022/02/28 23:23:30
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool valid(int s, int n, vector<vector<int>>& r) {
        vector<int> cnt(n, 0);
        for (int i = 0; i < r.size(); i++) {
            if ((s >> i) & 1) {
                cnt[r[i][0]]--;
                cnt[r[i][1]]++;
            }
        }
        for (int i = 0; i < n; i++) {
            if (cnt[i] != 0) return false;
        }
        return true;
    }

    int bits(int s) {
        int ans = 0;
        while(s) {
            ans++;
            s = s & (s-1);
        }
        return ans;
    }

    int maximumRequests(int n, vector<vector<int>>& requests) {
        int r = requests.size();
        int st = (1 << r) - 1;
        int ans = 0;
        for (int s = 1; s <= st; s++) {
            if (bits(s) <= ans) continue;
            if (valid(s, n, requests)) {
                ans = bits(s);
            }
        }
        return ans;
    }
};