// 剑指 Offer 49. 丑数
// https://leetcode-cn.com/problems/chou-shu-lcof/
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
@File : offer49.cpp
@Time : 2021/12/24 11:26:45
@Author : YuMin Zhang
@State : Half-Depedent
@Thinking :
@Tag : Medium
**/
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> ans{1};
        int a = 0, b = 0, c = 0;
        int num = 1;
        while(num < n) {
            int n2 = ans[a] * 2, n3 = ans[b] * 3, n5 = ans[c] * 5;
            ans.push_back(min(min(n2, n3), n5));
            if(ans[num] == n2) a++;
            if(ans[num] == n3) b++;
            if(ans[num] == n5) c++;
            num++;
        }
        return ans[num - 1];

    }
};