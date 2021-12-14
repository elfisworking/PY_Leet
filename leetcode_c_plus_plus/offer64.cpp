// 剑指 Offer 64. 求1+2+…+n
// https://leetcode-cn.com/problems/qiu-12n-lcof/
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
@File : offer64.cpp
@Time : 2021/12/14 20:46:06
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : 通过逻辑短路来进行逻辑判断
**/
class Solution {
public:
    int sumNums(int n) {
        n && (n += sumNums(n - 1));
        return n;
    }
};
