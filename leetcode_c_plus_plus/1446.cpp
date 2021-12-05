// 1446. 连续字符
// https://leetcode-cn.com/problems/consecutive-characters/
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
@File : 1446.cpp
@Time : 2021/12/01 14:26:37
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    int maxPower(string s) {
        int left = 0, right = 0;
        int ans = 0;
        while(right < s.size()) {
            while(right < s.size() && s[left] == s[right]) right++;
            ans = max(ans, right - left);
            left = right;
        }
        return ans;

    }
};