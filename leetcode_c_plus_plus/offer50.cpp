// 剑指 Offer 50. 第一个只出现一次的字符
// https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
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
@File : offer50.cpp
@Time : 2021/11/30 19:48:40
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/

class Solution {
public:
    char firstUniqChar(string s) {
        unordered_map<int, int> frequency;
        for (char ch: s) {
            ++frequency[ch];
        }
        for (int i = 0; i < s.size(); ++i) {
            if (frequency[s[i]] == 1) {
                return s[i];
            }
        }
        return ' ';
    }
};
