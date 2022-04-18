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
@File : 386.cpp
@Time : 2022/04/18 20:04:10
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans(n);
        int number = 1;
        for(int i = 0; i < n; i++) {
            ans[i] = number;
            if(number * 10 <= n) {
                number *= 10;
            } else {
                while(number % 10 == 9 || number + 1 > n) {
                    number /= 10;
                }
                number++;
            }
        }
        return ans;
        
    }
};