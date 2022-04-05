// 1346. 检查整数及其两倍数是否存在
// https://leetcode-cn.com/problems/check-if-n-and-its-double-exist/
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
@File : 1346.cpp
@Time : 2022/04/02 22:14:20
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int> set;
        for(auto x : arr) {
            int a = x * 2;
            if(set.count(a)) {
                return true;
            }
            if(x % 2 == 0) {
                if(set.count(x / 2)) return true;
            }
            set.insert(x);
        }
        return false;
    }
};