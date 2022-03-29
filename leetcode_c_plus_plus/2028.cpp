// 2028. 找出缺失的观测数据
// https://leetcode-cn.com/problems/find-missing-observations/
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
@File : 2028.cpp
@Time : 2022/03/27 21:06:51
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int sum = accumulate(rolls.begin(), rolls.end(), 0);
        int m = rolls.size();
        int total = mean * (n + m);
        vector<int> ans;
        int sub = total - sum;
        // cout << sub << endl;
        if(sub <= 0) {
            return ans;
        }
        
        int a = sub / n;
        int b = sub % n;
        // cout << a << b << endl;
        if(a == 0 || a > 6) {
            return ans;
        }
        for(int i = 0; i < n; i++) {
            ans.push_back(a);
        }
        int index = 0;
        while(b) {
            if(ans[index % n] + 1 <= 6) {
                ans[index % n] += 1;
                b--;
                index++;
            } else {
                return vector<int>{};
            }
        }
        return ans;
    }
};