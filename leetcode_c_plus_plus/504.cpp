// 504. 七进制数
// https://leetcode-cn.com/problems/base-7/submissions/
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
@File : 504.cpp
@Time : 2022/03/07 23:04:28
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    string convertToBase7(int num) {
        if(num == 0) return "0";
        bool flag = false;
        if(num < 0) {
            flag = true;
            num = abs(num);
        }
        string ans = "";
        while(num > 0) {
            ans += to_string(num % 7);
            num = num / 7;
        }
        if(flag) ans += "-";
        reverse(ans.begin(), ans.end());
        return ans;

    }
};