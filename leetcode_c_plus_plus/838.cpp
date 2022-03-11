// 838. 推多米诺
// https://leetcode-cn.com/problems/push-dominoes/
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
@File : 838.cpp
@Time : 2022/02/21 21:39:45
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    string pushDominoes(string dominoes) {
        int n = dominoes.size(), i = 0;
        char left = 'L';
        while(i < n) {
            int j = i;
            while(j < n && dominoes[j] == '.') j++;
            char right = j < n ? dominoes[j] : 'R';
            if(left == right) {
                while(i < j) {
                    dominoes[i++] = right;
                }
            } else if(left == 'R' && right == 'L') {
                int k = j - 1;
                while(i < k) {
                    dominoes[i++] = 'R';
                    dominoes[k--] = 'L'; 
                }
            }
            left = right;
            i = j + 1;
        }
        return dominoes;
    }
};
