// 233. 数字 1 的个数
// https://leetcode-cn.com/problems/number-of-digit-one/
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
@File : 233.cpp
@Time : 2022/03/25 15:16:40
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int countDigitOne(int n) {
        long long mulk = 1;
        int ans = 0;
        for(int k = 0; n >= mulk; k++) {
            ans += (n / (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk + 1, 0LL), mulk);
            mulk = 10 * mulk;
        }
        return ans;

    }
};