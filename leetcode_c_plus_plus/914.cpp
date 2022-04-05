// 914. 卡牌分组
// https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/
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
@File : 914.cpp
@Time : 2022/04/01 11:38:30
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        unordered_map<int, int> map;
        for(auto x : deck) {
            map[x]++;
        }
        int gcd_num = -1;
        for(auto [_, v] : map) {
            if(gcd_num == -1) {
                gcd_num = v;
            } else {
                gcd_num = gcd(gcd_num, v);
            }
        }
        return gcd_num >= 2;
    }


    int gcd(int a, int b) {
        return b ? gcd(b, a %b) : a;
    }
};