// 1025. 除数博弈
// https://leetcode-cn.com/problems/divisor-game/
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
@File : 1025.cpp
@Time : 2022/03/26 15:07:52
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool divisorGame(int n) {
        // whose get 2, that win
        int mod= n % 10;
        if(mod% 2 == 0) {
            return true;
        }
        return false;
    }
};