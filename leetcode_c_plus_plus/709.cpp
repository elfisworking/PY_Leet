// 709. 转换成小写字母
// https://leetcode-cn.com/problems/to-lower-case/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : 709.cpp
@Time : 2021/12/12 20:06:22
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    string toLowerCase(string s) {
        for(char & ch : s) {
            if( ch >= 'A' && ch <= 'Z')
                ch |= 32;
        }
        return s;
    }
};