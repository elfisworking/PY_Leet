// 剑指 Offer 62. 圆圈中最后剩下的数字
// https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
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
@File : offer62.cpp
@Time : 2021/12/19 12:50:19
@Author : YuMin Zhang
@State : Depedent 
@Thinking : 约瑟夫环  反推
@Tag : Easy 
**/

class Solution {
public:
    int lastRemaining(int n, int m) {
        int ans = 0;
        for(int i = 2; i <= n; i++) {
            ans = (ans + m) % i;
        }
        return ans;


    }
};