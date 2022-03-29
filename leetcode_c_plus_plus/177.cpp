// 172. 阶乘后的零
// https://leetcode-cn.com/problems/factorial-trailing-zeroes/
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
@File : 177.cc
@Time : 2022/03/25 14:15:08
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int trailingZeroes(int n) {
        int ans = 0;
        while(n) {
            n = n / 5;
            ans += n;
        }
        return ans;
    }
};