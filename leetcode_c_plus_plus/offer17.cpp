// 剑指 Offer 17. 打印从1到最大的n位数
// https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
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
@File : offer17.cpp
@Time : 2021/12/25 18:20:42
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
**/
class Solution {
public:
    vector<int> printNumbers(int n) {
        int num = pow(10, n);
        vector<int> ans;
        for(int i =1; i < num; i++) {
            ans.push_back(i);
        }
        return ans;

    }
};