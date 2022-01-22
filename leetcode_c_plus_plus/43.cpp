// 43. 字符串相乘
// https://leetcode-cn.com/problems/multiply-strings/
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
@File : 43.cpp
@Time : 2022/01/20 21:59:40
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
**/
class Solution {
public:
    string multiply(string num1, string num2) {
        if(num1 == "0" || num2 == "0") return "0";
        int n = num1.size(), m = num2.size();
        string ans = "0";
        for(int i = n -1; i >=0; i--) {
            int carry = 0;
            string curr;
            int y = num1[i] - '0';
            for(int t = 0; t < n - i - 1; t++) {
                curr.push_back('0');
            }
            for(int j = m - 1; j >=0; j--) {
                int product = (num2[j] - '0') * y + carry;
                carry = product / 10;
                curr.push_back(product % 10 + '0');
            }
            if(carry > 0) curr.push_back(carry + '0');
            reverse(curr.begin(), curr.end());
            ans = addString(ans, curr);
        }
        return ans;
    }
    
    string addString(string num1, string num2) {
        int i = num1.size() - 1, j = num2.size() - 1;
        int carry = 0;
        string ans;
        while(i >=0 || j >=0 || carry != 0) {
            int x = i >=0 ? num1[i] - '0' : 0;
            int y = j >=0 ? num2[j] - '0' : 0;
            int add =  x  + y + carry;
            carry = add / 10;
            ans.push_back(add % 10 + '0');
            i--;
            j--;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
