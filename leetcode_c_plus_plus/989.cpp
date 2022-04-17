// 989. 数组形式的整数加法
// https://leetcode-cn.com/problems/add-to-array-form-of-integer/
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
@File : 989.cpp
@Time : 2022/04/06 20:55:13
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        vector<int> ans;
        int l = num.size();
        int right = l - 1;
        int carry = 0;
        while(right >= 0 || k > 0 || carry > 0) {
            int a = right >= 0 ? num[right] : 0;
            int b = k > 0 ? k % 10 : 0;
            int c = a + b + carry;
            carry = c / 10;
            c = c % 10;
            ans.push_back(c);
            k /= 10;
            right--;
        }
        reverse(ans.begin(), ans.end());
        return ans;

    }
};