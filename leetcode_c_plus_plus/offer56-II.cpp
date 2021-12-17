//
//
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
@File : offer56-II.cpp
@Time : 2021/12/17 14:01:31
@Author : YuMin Zhang
@State : Depedent 
@Thinking :
@Tag : Medium
**/
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int counts[32] = {0};
        
        for(int num : nums) {
            for(int j = 0; j < 32; j++) {
                counts[j] += num & 1;
                num >>= 1;
            }
    }

        int res = 0;
        for(int i = 0; i < 32; i++) {
            res <<= 1;
            res |= (counts[31 - i] % 3);
            
        }
        return res;
    }
};