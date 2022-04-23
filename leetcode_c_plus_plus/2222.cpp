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
@File : 2222.cpp
@Time : 2022/04/19 22:52:07
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/

#define ll long long
class Solution {
public:
    long long numberOfWays(string s) {
        int n = s.size();
        if(n < 3) return 0;
        vector<int> left_one(n, 0);
        vector<int> right_one(n, 0);
        vector<int> left_zero(n, 0);
        vector<int> right_zero(n, 0);
        if(s[0] == '1') {
            left_one[0] = 1;
        } else {
            left_zero[0] = 1;
        }

        for(int i = 1; i < n; i++) {
            if(s[i] == '0') {
                left_one[i] = left_one[i - 1];
                left_zero[i] = left_zero[i - 1] + 1;
            } else {
                left_one[i] = left_one[i - 1] + 1;
                left_zero[i] = left_zero[i - 1];
            }
                // printf("%d, %d\n", left_one[i], left_zero[i]);
        }
        if(s[n - 1] == '1') {
            right_one[n - 1] = 1;
        } else {
            right_zero[n - 1] = 1;
        }
        for(int i = n - 2; i >= 0; i--) {
            if(s[i] == '0') {
                right_one[i] = right_one[i + 1];
                right_zero[i] = right_zero[i + 1] + 1;
            } else {
                right_one[i] = right_one[i + 1] + 1;
                right_zero[i] = right_zero[i + 1];
            }
                // printf("%d, %d\n", right_one[i], right_zero[i]);
        }
        ll ans;
        for(int i = 0; i < n; i++) {
            if(s[i] == '1') {
                //printf("%d, %d\n", left_zero[i], right_zero[i]);
                ans += (left_zero[i] * right_zero[i]);
            } else {
                //printf("%d, %d\n", left_one[i], right_one[i]);
                ans += (right_one[i] * left_one[i]);
            }
        }
        return ans;
    }
};
int main() {
    Solution s;
    s.numberOfWays("001101");
}