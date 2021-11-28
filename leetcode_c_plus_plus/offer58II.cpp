// 剑指 Offer 58 - II. 左旋转字符串
// https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer58II.cpp
@Time : 2021/11/28 21:56:04
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/

class Solution {
public:
    string reverseLeftWords(string s, int n) {
        string sub = s.substr(0,n);
        string sub_1 = s.substr(n,s.size() - n);
        return sub_1 + sub;
    }
};