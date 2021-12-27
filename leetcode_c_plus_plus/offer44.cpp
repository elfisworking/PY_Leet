// 剑指 Offer 44. 数字序列中某一位的数字
// https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
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
@File : offer44.cpp
@Time : 2021/12/27 21:28:30
@Author : YuMin Zhang
@State : Half-Depedent
@Thinking :
@Tag : Medium
**/
class Solution {
public:
    int findNthDigit(int n) {
        if(n < 10) return n;
        n = n - 10;
        long long num = 90;
        int k = 2;
        while(n > num * k) {
            n -= num * k;
            num *= 10;
            k++;
        }
        int base = pow(10, k - 1);
        int i = n / k, j = n % k;
        cout << base << i << endl;
        string ans = to_string(base + i);
        return ans[j] - '0';


    }
};