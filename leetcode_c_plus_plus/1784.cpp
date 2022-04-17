//
//
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
@File : 1784.cpp
@Time : 2022/04/06 21:07:57
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    bool checkOnesSegment(string s) {
        char prev = s[0];
        int count = 0;
        for(int i = 1; i < s.size(); i++) {
            if(prev == '1' && s[i] == '0') {
                count++;
            }
            prev = s[i];
        }
        if(prev == '1') count++;
        return count <= 1 ? true : false;
    }
};