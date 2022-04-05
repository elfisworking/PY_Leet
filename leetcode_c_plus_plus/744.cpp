// 744. 寻找比目标字母大的最小字母
// https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/
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
@File : 744.cpp
@Time : 2022/04/03 15:36:19
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        for(auto ch : letters){
            if(ch > target) return ch;
        }
        return letters[0];
    }
};