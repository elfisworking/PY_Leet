// 剑指 Offer 10- II. 青蛙跳台阶问题
// https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
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
@File : offer10-II.cpp
@Time : 2021/12/05 19:18:38
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    int numWays(int n) {
        if( n  <= 1) return 1;
        int a = 1, b = 1;
        for(int i = 2; i <= n; i++) {
            int sum = (a + b) % 1000000007;
            b = a;
            a = sum;
        }
        return a;
    }
};
