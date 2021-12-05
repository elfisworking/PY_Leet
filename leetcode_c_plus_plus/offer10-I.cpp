// 剑指 Offer 10- I. 斐波那契数列
// https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
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
@File : offer10-I.cpp
@Time : 2021/12/05 19:12:20
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    int fib(int n) {
        if(n < 1)
        {
            return n;
        }

        int pre = 0, cur = 1;
        for(int i = 2; i <= n; ++i)
        {
            int sum = pre + cur;
            pre = cur;
            cur = sum % 1000000007;
        }

        return cur;
    }
};