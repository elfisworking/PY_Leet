// 2024. 考试的最大困扰度
// https://leetcode-cn.com/problems/maximize-the-confusion-of-an-exam/
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
@File : 2024.cpp
@Time : 2022/03/29 20:39:56
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int l = 0;
        int T = 0;
        int F = 0;
        int ans = 0;
        for(int i = 0; i < answerKey.size(); i++) {
            if(answerKey[i] == 'T') {
                T++;
            } else {
                F++;
            }
            while(min(T, F) > k) {
                if(answerKey[l] == 'T') T--;
                else F--;
                l++; 
            }
            ans = max(ans, i - l + 1);
        }
        return ans;
        
    }
};