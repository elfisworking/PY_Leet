//  598. 范围求和 II
// https://leetcode-cn.com/problems/range-addition-ii/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
/**
@File : 598.cpp
@Time : 2021/11/07 14:40:38
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        int a = m;
        int b = n;
        for(auto & i : ops) {
            a = min(a, i[0]);
            b = min(b, i[1]);
        }
        return a * b;
    }
};