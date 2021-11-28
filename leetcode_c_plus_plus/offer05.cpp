// 剑指 Offer 05. 替换空格
// https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer05.cpp
@Time : 2021/11/28 22:02:38
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/

class Solution {
public:
    string replaceSpace(string s) {
        string ans;
        for(char ch : s) {
            if(ch == ' ') {
                ans.push_back('%');
                ans.push_back('2');
                ans.push_back('0');
            } else {
                ans.push_back(ch);
            }
        }
        return ans;
    }
};