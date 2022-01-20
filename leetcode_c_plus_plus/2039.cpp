// 2029. 石子游戏 IX
// https://leetcode-cn.com/problems/stone-game-ix/
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
@File : 2039.cpp
@Time : 2022/01/20 11:14:09
@Author : YuMin Zhang
@State : depeedent
@Thinking :
@Tag : Medium
**/class Solution {
public:
    bool stoneGameIX(vector<int>& stones) {
        bool Awin = true, Bwin = false;
        if(stones.size() == 1) return Bwin;
        vector<int> cnt(3, 0);
        for(auto x : stones) {    //模3预处理
            cnt[x % 3]++;
        }
        if(cnt[1] == 0 && cnt[2] == 0) return Bwin; //全是3的倍数，谁先动谁输
        //成对的三的倍数大家相互取，相当于可以抵消不用管
        if(cnt[0] % 2 == 0) { 
            //偶数个，相当于没3，如果有1，2A必赢，选定1或2中一个后，后续的保证不输的序列是固定的，哪个能赢用哪个，前提是有1，2可选
            return (cnt[1] != 0 && cnt[2] != 0) ? Awin : Bwin;
        }
        else {  //奇数个，相当于可以颠倒先后手，前提是个数够颠倒，成对的1，2可以相互抵消
            int remain = max(cnt[1], cnt[2]) - min(cnt[1], cnt[2]);
            //如果剩余的足够颠倒，A可以在1，2中选择必赢策略
            return remain > 2 ? Awin : Bwin;
        }
    }
};

